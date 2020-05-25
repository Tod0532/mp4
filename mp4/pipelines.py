# -*- coding: utf-8 -*-
import urllib.request

import requests

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

number=1
class Mp4Pipeline(object):
    def process_item(self, item, spider):
        global number
        number = number+1
        for j in range(0,len(item["mp4url"])):
            print(item["mp4url"][j])
            localpath = "E:/100_Python/120_Program/V2/"+str(number)+str(j) + ".mp4"
            urllib.request.urlretrieve(item["mp4url"][j], filename=localpath)
            print(str(number)+str(j)+"=====>saved")
        return item

