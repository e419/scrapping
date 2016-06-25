#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Sample search item """

import scrapy

class SearchItem(scrapy.Item):
    """ Sample search result to be saved """
    title = scrapy.Field()
    link = scrapy.Field()
