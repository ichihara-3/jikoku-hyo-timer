# -*- coding: utf-8 -*-
import datetime
import logging
from typing import Tuple

import scrapy

from kyotosubway.items import KyotosubwayItem


class Schedule:

    def __init__(self, name: str, tags: Tuple[str]):
        self.name = name
        self.tags = tags


class KarasumalineSpider(scrapy.Spider):
    name = 'karasumaline'
    linename = '烏丸線'
    schedule_types = (
        Schedule('平日', (
            'table tr.time.wektime',
            'td.heijitsu-tt h3::text',
             'span.disptnwek',
            )),
        Schedule('土休日',
            (
            'table tr.time.holtime',
            'td.kyujitsu-tt h3::text',
             'span.disptnhol',
            )),
    )
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
        for schedule_type in self.schedule_types:
            timetable=KyotosubwayItem(
                station=response.css('div.tt-hed-title::text').get(),
                line=self.linename,
                direction=updown,
                departures=[],
            )
            timetable['train_schedule_type'] = schedule_type.name
            for line in response.css(schedule_type.tags[0]):
                hour = line.css(schedule_type.tags[1]).get()
                for td in line.css('td'):
                    for span in td.css(schedule_type.tags[2]):
                        for minute in span.css('::text').getall():
                            if minute.isdigit():
                                break
                        else:
                            continue
                        dest_keyword = span.css('span span span::text').get()
                        timetable['departures'].append(Departure(hour=int(hour), minute=int(minute), dest_keyword=dest_keyword, updown=updown))
            yield timetable


class Destinations:

    destination_map = {
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
        return cls.destination_map.get(updown, {}).get(keyword, None)


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

