#-*- coding: UTF-8 -*-
# Scrapy settings for pic_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pic_spider'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['pic_spider.spiders']
NEWSPIDER_MODULE = 'pic_spider.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['pic_spider.pipelines.PicSpiderPipeline']  # ImagePipeline的自定义实现类
IMAGES_STORE = 'E:\\WUSZ\\py_prj\\scrapy\\images'   # 图片存储路径
IMAGES_EXPIRES = 90                                   # 过期天数
IMAGES_MIN_HEIGHT = 100                               # 图片的最小高度
IMAGES_MIN_WIDTH = 100                                # 图片的最小宽度
# 图片的尺寸小于IMAGES_MIN_WIDTH*IMAGES_MIN_HEIGHT的图片都会被过滤

