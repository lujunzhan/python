# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt,xlrd

class DoubanPipeline(object):

    def __init__(self):
        pass

    def open_spider(self,spider):
        self.filename = "豆瓣电影top250.xls"
        self.book = xlwt.Workbook(encoding="utf8")
        self.sheet = self.book.add_sheet('豆瓣电影')
        head = ['电影名称','评分','评价人数','导演','主演','类型','描述']

        for h in head:
            self.sheet.write(0, head.index(h), h)

        self.l = 1

    def process_item(self, item, spider):

        j = 0
        for k,v in item.items():
            line = self.l
            for i in range(len(v)):
                self.sheet.write(line,j,v[i])
                line +=1
            j += 1

        self.l= self.l + 25

        return item

    def close_spider(self,spider):
        self.book.save(self.filename)