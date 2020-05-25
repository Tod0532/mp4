# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mp4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mp4url = scrapy.Field()
    mp4id = scrapy.Field()

