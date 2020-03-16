# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from sqlalchemy import create_engine

class KyotosubwayPipeline(object):

    def open_spider(self, spider):
        self.engine = create_engine('postgresql://postgres:pass@localhost:5432/transportation')

    def close_spider(self, spider):
        self.engine.close()

    def process_item(self, item, spider):
        con = self.engine.connect()
        trans = con.begin()
        try:
            for departure in item['departures']:
                SQL = '''
                INSERT INTO timetables_name
                (station, line, train_schedule_type, direction, destination, departure_time)
                VALUES (%s, %s, %s, %s, %s, %s)
                '''
                data = (item['station'], item['line'], item['train_schedule_type'], item['direction'], departure.destination, str(departure))
                con.execute(SQL, data)
            trans.commit()
        except:
            trans.rollback()
            raise
