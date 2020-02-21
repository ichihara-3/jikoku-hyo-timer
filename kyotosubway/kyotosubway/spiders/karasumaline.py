# -*- coding: utf-8 -*-
import datetime
import logging
import scrapy


class KarasumalineSpider(scrapy.Spider):
    name = "karasumaline"
    allowed_domains = ["www2.city.kyoto.lg.jp"]
    start_urls = ["http://www2.city.kyoto.lg.jp/kotsu/tikadia/hyperdia/line02.htm"]

    def parse(self, response):
        # # 上り
        # for a in response.css("td a[title*=国際会館方面]"):
        #     yield response.follow(
        #         a, cb_kwargs={"updown": "上り"}, callback=self.parse_table
        #     )
        # 下り
        for a in response.css("td a[title*=近鉄奈良方面]"):
            yield response.follow(
                a, cb_kwargs={"updown": "下り"}, callback=self.parse_table
            )

    def parse_table(self, response, updown):
        timetable = {
            "station": " ".join(response.css("div.tt-hed-title::text").extract())
            + "方面 "
            + "(" + updown + ")",
            "times": [],
        }
        for line in response.css("table tr.time.wektime"):
            hour = line.css("td.heijitsu-tt h3::text").get()
            for td in line.css("td"):
                for span in td.css("span.disptnwek"):
                    minute = span.css('::text').get()
                    if not minute.isdigit():
                        continue
                    dest_keyword = span.css('span span span::text').get()
                    logging.debug(dest_keyword)
                    departure = Departure(hour=int(hour), minute=int(minute), destination=dest_keyword)
                    timetable["times"].append({'time': departure.time.strftime('%H:%M'), 'dest': departure.destination})

        yield timetable


class Departure:
    def __init__(self, **kwargs):
        self._hour: int = kwargs.get("hour") % 24
        self._minute: int = kwargs.get("minute") % 60
        self._destination: String = kwargs.get("destination")

    def __str__(self):
        return self.time.strftime('%H:%M')

    @property
    def time(self) -> datetime.time:
        return datetime.time(hour=self._hour, minute=self._minute)

    @property
    def destination(self) -> str:
        return self._destination
