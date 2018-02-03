# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class DBPipeline(object):
    def process_item(self, item, spider):
        #print('DBPipeline',item) # # 新闻1：标题和url； # 新闻2：标题和url
        return item
        # raise DropItem()

class FilePipeline(object):
    def __init__(self):
        self.f = None

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('开始....')
        self.f = open('xxxx.log','a+',encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item['text']+'\n')
        self.f.flush()
        return item

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.f.close()
        print('结束')


