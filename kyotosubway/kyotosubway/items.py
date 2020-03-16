# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KyotosubwayItem(scrapy.Item):
    station = scrapy.Field()
    line = scrapy.Field()
    train_schedule_type = scrapy.Field()
    direction = scrapy.Field()
    departures = scrapy.Field()
