# *-* coding: UTF-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from tutorial.items import DmozItem

from scrapy.http import Request

class DmozSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/top250"
    ]

    def parse(self, response):

        hxs = HtmlXPathSelector(response)
        # hxs.select('//li/div/div/div/a/span[@class="title"]/text()').extract()[0]
        # hxs.select('//li/div/div/div/p/span[@class="inq"]/text()').extract()[0]
        sites = hxs.select('//li/div/div[@class="info"]')
        items = []
        for site in sites:
            item = DmozItem()         
            item['movie'] = site.select('div[@class="hd"]/a/span[@class="title"]/text()').extract()
            item['note'] = site.select('div[@class="bd"]/p/span[@class="inq"]/text()').extract()
            yield item
        #     items.append(item)
        # return items
        url = hxs.select('//a[contains(text(),"后页")]/@href').extract()
        if url:
            page = 'https://movie.douban.com/top250' + url[0]
            yield Request(page, callback=self.parse)
        
        
        
        