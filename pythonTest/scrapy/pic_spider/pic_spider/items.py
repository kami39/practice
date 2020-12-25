# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PicSpiderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pic_urls = Field()
    pic_name = Field()
    pic_paths = Field()

if __name__ == '__main__':
 	print dir(PicSpiderItem)
 	print "----------------"
 	print PicSpiderItem.__class__
 	# print PicSpiderItem.__base__
 	print "----------------"
 	print Field.__class__
