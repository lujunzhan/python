# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from  ..items import DoubanImgItem
from scrapy.pipelines.images import ImagesPipeline


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'https://movie.douban.com/top250'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = DoubanImgItem()
        item['image_urls'] = response.xpath(".//div[@class='pic']/a/img/@src ").extract()

        yield  item


