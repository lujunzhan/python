# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoubanspiderSpider(CrawlSpider):
    name = 'db'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'https://movie.douban.com/top250'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        item['movie'] = response.xpath(".//span[@class='title'][1]//text()").extract()
        item['star'] = response.xpath(".//div[@class = 'star']/span[2]/text()").extract()
        item['evaluate_num'] = response.xpath(".//div[@class = 'star']/span[4]/text()").extract()
        item['diretor'] = response.xpath(".//div[@class='bd']/p/text()").extract()
        item['actor'] = []
        item['type'] = []
        item['quote'] = response.xpath(".//div[@class='bd']/p[2]/span/text()").extract()

        """-- 处理item['director]中的字符串问题 --"""
        for i in item['diretor']:
            str = "".join(i.split())
            item['diretor'][item['diretor'].index(i)] = str

        # 去掉列表中的空项
        while '' in item['diretor']:
            item['diretor'].remove('')

        # print("test:",item['diretor'])

        """"-- 导演与类型进行分离 --"""
        count = 1
        for i in item['diretor']:

            temp = item['diretor'].pop(count)
            item['type'].append(temp)

            count +=1


        """-- 将导演和主演进行分开 -- """
        count = 0
        diretor = []
        actor = []
        for i in range(len(item['diretor'])):
            temp = item['diretor'][count].split("导演:", 2)[1]

            if "主演:" not in temp:
                diretor.append(temp)
                actor.append("暂无")
                count += 1
                continue

            temp = temp.split("主演:",2)
            diretor.append(temp[0])
            actor.append(temp[1])

            count+=1

        # 将处理好的数据放回item中
        item['diretor'] = diretor
        item['actor'] = actor

        yield item
