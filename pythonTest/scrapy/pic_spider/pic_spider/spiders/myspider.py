#-*- coding: UTF-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from pic_spider.items import PicSpiderItem
import urllib
from scrapy.http import Request


class pic_Spider(BaseSpider):
    name = "pic_spider"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/top250",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//div[@class="pic"]')
        
        items = []
        
        for img in imgs:
            item = PicSpiderItem()
            item['pic_urls'] = img.select('a/img/@src').extract()
            item['pic_name'] = img.select('a/img/@alt').extract()
            # print (item['pic_urls'] )
            urllib.urlretrieve(item['pic_urls'][0],'E:/WUSZ/py_prj/scrapy/images/'+'%s.jpg'%item['pic_name'][0])
            
            yield item

        url = hxs.select('//a[contains(text(),"后页")]/@href').extract()
        if url:
            page = 'https://movie.douban.com/top250' + url[0]
            yield Request(page, callback=self.parse)

if __name__ == "__main__":
    print dir(HtmlXPathSelector)
    print HtmlXPathSelector.__class__
