# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DmozItem(Item):
    # link = Field()
    # desc = Field()
    movie = Field()
    note = Field()

