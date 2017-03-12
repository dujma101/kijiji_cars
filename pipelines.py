# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# Save data to sqllit
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/0.18/topics/item-pipeline.html
import sqlite3
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
class KijijiCarsPipeline(object):
    filename='cars.db'

    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)

    def initialize(self):
        if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            self.conn=self.create_table(self.filename)
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute('''CREATE TABLE IF NOT EXISTS cars (
id integer primary key autoincrement,
listed text,
make text,
model text,
year integer,
kilometers integer,
price integer,
address text,
transmission  text,
body_type text,
color text,
doors integer,
drivetrain text,
fuel_type text,

description text,
link text,
seller text)
''')
        conn.commit()
        return conn

    def process_item(self,item,spider):
        print('[[[[[[[[[[[[[[[[[[[[[[[[[[[item',item)
        print('3333333333333333333333',item['Date Listed'])
        print(type(item))
        self.conn.execute("INSERT INTO cars  VALUES (?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(None ,item['Date Listed'], item['Make'], item['Model'], item['Year'], item['Kilometers'], item['Price'], item['Address'][:-8], item['Transmission'], item['Body Type'], item['Colour'], item['No. of Doors'], item['Drivetrain'], item['Fuel Type'],  item['Description'],  item['Url'], item['For Sale By']))
        self.conn.commit()
        return item