# -*- coding: utf-8 -*-
import scrapy


class KarasumalineSpider(scrapy.Spider):
    name = 'karasumaline'
    allowed_domains = ['www2.city.kyoto.lg.jp']
    start_urls = ['http://www2.city.kyoto.lg.jp/kotsu/tikadia/hyperdia/line02.htm']

    def parse(self, response):
        # 上り
        for a in response.css('td a[title*=国際会館方面]'):
            yield response.follow(a, cb_kwargs={'updown': "上り"},callback=self.parse_table)
        # 下り
        for a in response.css('td a[title*=近鉄奈良方面]'):
            yield response.follow(a, cb_kwargs={'updown': "下り"}, callback=self.parse_table)

    def parse_table(self, response, updown):
        timetable = {
            'station': ' '.join(response.css('div.tt-hed-title::text').extract()) + updown + '方面',
            'times': {}
        }
        for line in response.css('table tr.time.wektime'):
            hour = line.css('td.heijitsu-tt h3::text').get()
            timetable['times'][hour] = []
            for minute in line.css('td'):
                timetable['times'][hour].extend(minute.css('span.disptnwek::text').getall())
        yield timetable
