#-*- coding:utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'booksspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_book)

        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield  scrapy.Request(next_url,callback=self.parse)

    def parse_book(self,response):
        book = BookItem()
        sel = response.css('div.product_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')

        yield book

        #books_name = response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@title').extract()
        #for i_item in books_name:
         #   print(i_item)
       # books_price = response.xpath('//*[@id="default"]/div/div/div/div/section/div/ol/li/article/div/p[1]/text()').extract()
       # for i in books_price:
       #     print(i)
        #books_rank = response.xpath('//')
