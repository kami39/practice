#-*- coding: UTF-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
import codecs

class TutorialPipeline(object):
    # def process_item(self, item, spider):
    #     return item
	def __init__(self):
		self.file = codecs.open('TOP250', 'w', encoding='UTF-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line.decode('unicode_escape'))
		return item
	
	def open_spider(self, spider):
		pass
	
	def close_spider(self, spider):
		pass
