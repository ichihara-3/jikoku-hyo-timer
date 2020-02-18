# -*- coding: utf-8 -*-
import scrapy


class KarasumalineSpider(scrapy.Spider):
    name = 'karasumaline'
    allowed_domains = ['www2.city.kyoto.lg.jp']
    start_urls = ['http://www2.city.kyoto.lg.jp/kotsu/tikadia/hyperdia/line02.htm']

    def parse(self, response):
        # 上り
        for a in response.css('td a[title*=国際会館方面]'):
            yield {'href': a.attrib.get('href')}
        # 下り
        for a in response.css('td a[title*=近鉄奈良方面]'):
            yield {'href': a.attrib.get('href')}

    def parse_table(self, response):
        pass
