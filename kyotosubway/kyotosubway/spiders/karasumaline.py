# -*- coding: utf-8 -*-
import datetime
import logging
import scrapy


class KarasumalineSpider(scrapy.Spider):
    name = 'karasumaline'
    allowed_domains = ['www2.city.kyoto.lg.jp']
    start_urls = ['http://www2.city.kyoto.lg.jp/kotsu/tikadia/hyperdia/line02.htm']

    def parse(self, response):
        # 上り
        for a in response.css('td a[title*=国際会館方面]'):
            yield response.follow(
                a, cb_kwargs={'updown': '上り'}, callback=self.parse_table
            )
        # 下り
        for a in response.css('td a[title*=近鉄奈良方面]'):
            yield response.follow(
                a, cb_kwargs={'updown': '下り'}, callback=self.parse_table
            )

    def parse_table(self, response, updown):
        timetable = {
            'station': response.css('div.tt-hed-title::text').get(),
            'up_or_down': updown,
            'departures': [],
        }
        for line in response.css('table tr.time.wektime'):
            hour = line.css('td.heijitsu-tt h3::text').get()
            for td in line.css('td'):
                for span in td.css('span.disptnwek'):
                    minute = span.css('::text').get()
                    if not minute.isdigit():
                        continue
                    dest_keyword = span.css('span span span::text').get()
                    departure = Departure(hour=int(hour), minute=int(minute), dest_keyword=dest_keyword, updown=updown)
                    timetable['departures'].append({'time': departure.time.strftime('%H:%M'), 'dest': departure.destination})
        yield timetable


class Destinations:

    _stations_map = {
        '下り': {
            '新': '普通 新田辺行き',
            '奈': '急行 近鉄奈良行き',
            None: '竹田行き'
        },
        '上り': {
            None: '国際会館行き'
        }
    }

    @classmethod
    def get_destionation_by(cls, updown='上り', keyword=None):
        return cls._stations_map.get(updown, {}).get(keyword, None)

class Departure:
    def __init__(self, hour: int, minute: int, dest_keyword: str, updown: str):
        self._hour: int = hour % 24
        self._minute: int = minute % 60
        self._dest_keyword: str = dest_keyword
        self._updown: str = updown

    def __str__(self) -> str:
        return self.time.strftime('%H:%M')

    @property
    def time(self) -> datetime.time:
        return datetime.time(hour=self._hour, minute=self._minute)

    @property
    def destination(self) -> str:
        return Destinations.get_destionation_by(updown=self._updown, keyword=self._dest_keyword)

