# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class BooksSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    books_name = scrapy.Field()
    books_price = scrapy.Field()
    books_pic = scrapy.Field()
    review_rating = scrapy.Field()
    review_num = scrapy.Field()

class BookItem(Item):
    name = Field()
    price = Field()
    review_rating = Field()
