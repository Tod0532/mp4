# -*- coding: utf-8 -*-
import scrapy

from mp4.items import Mp4Item
from scrapy.http import Request
import re

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['http://www.zzzttt.vip']
    start_urls = ['http://www.zzzttt.vip/archives/196.html/']

    def parse(self, response):
        item=Mp4Item()
        # 取实际地址存放在item中
        try:
            paturl = '(https://nim-nosdn.netease.im/.*?)"'
            item["mp4url"]=re.compile(paturl).findall(str(response.body))
            print(item["mp4url"])
            # 取名字
            patloacl ='<meta itemprop="headline" content="(.*?)">'
            item["mp4id"] = re.compile(patloacl).findall(str(response.body))
            print(item["mp4id"])
            # print(str(item["mp4id"][0].encoding('gbk'))
            yield item
        except:
            pass
        for i in range(220,310):
            print(i)
            nexturl="http://www.zzzttt.vip/archives/"+str(i)+".html"
            # dont_filter=True不过滤REQUEST.默认dont_filter=False它的目的就是过滤掉那些不在 allowed_domains 列表中的请求 requests。
            yield Request(nexturl,callback=self.parse,dont_filter=True)