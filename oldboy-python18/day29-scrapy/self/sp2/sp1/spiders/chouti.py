# -*- coding: utf-8 -*-
"""
scrapy scrawl chouti

# 找ChoutiSpider类，
根据start_urls去下载页面，当下载完成之后，自动执行parse函数。
"""

import scrapy
from scrapy.selector import HtmlXPathSelector
from ..items import Sp1Item

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/','http://dig.chouti.com/']

    def parse(self, response):
        # print('已经下载完成',response)
        # 1. 获取页面上所有的新闻，将标题和URL写入文件
        """
        // 表示从跟开始向下找标签
        //div[@id="content-list"]
        //div[@id="content-list"]/div[@class="item"]
        .// 相对当前对象

        """
        hxs = HtmlXPathSelector(response)
        item_list = hxs.select('//div[@id="content-list"]/div[@class="item"]')
        for item in item_list:
            # text = item.select('.//div[@class="part1"]/a/text()').extract() # ['xxxx','xxxx','xxxx']
            text1 = item.select('.//div[@class="part1"]/a/text()').extract_first().strip()
            url1 = item.select('.//div[@class="part1"]/a/@href').extract_first()
            # 新闻1：标题和url
            # 新闻2：标题和url
            yield Sp1Item(text=text1,url=url1)




