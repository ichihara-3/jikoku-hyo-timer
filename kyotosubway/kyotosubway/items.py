# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KyotosubwayItem(scrapy.Item):
    station = scrapy.Field()
    up_or_down = scrapy.Field()
    departures = scrapy.Field()
