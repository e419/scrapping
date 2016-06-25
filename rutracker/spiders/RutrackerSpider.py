#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Another try to implement scrappy spider for rutracker """


import os
import copy
import scrapy
from scrapy.http import FormRequest

from rutracker.items import SearchItem


LOGIN_URL = 'http://login.rutracker.org/forum/login.php'

SEARCH_URL = 'http://rutracker.org/forum/tracker.php'

creds = {
    'login':  u'Вход',
    'login_username': os.environ.get('TRACKER_USER', 'foo'),
    'login_password': os.environ.get('TRACKER_PASSWORD', 'bar')
}

search_item = {
    'nm': os.environ.get('TRACKER_SEARCH', 'idm 2016')
}

class RutrackerSpider(scrapy.Spider):
    """ Scrapper for rutracker 
    by default they give us 50 results per page
    """
    name = 'rutracker.org'
    start_urls = [LOGIN_URL]

    def parse(self, response):
        """ Initiate login """
        request = FormRequest(
            LOGIN_URL,
            formdata=creds,
            callback=self.after_login
        )
        return request

    def after_login(self, response):
        """ Getting content titles out of site
        
        Arguments:
        - `self`: scrapy.Spider instance
        - `response`: scrapy.Response object
        """
        request = FormRequest(
            SEARCH_URL,
            formdata=search_item,
            callback=self.generate_links
        )
        return request

    def generate_links(self, response):
        """ Get list of links to traverse """
        num_results_raw = response.xpath(
            '//p[2]/text()').extract()[0].strip()
        num_results_int = num_results_raw.encode('utf-8').replace(
            'Результатов поиска: ', '')
        try:
            num_results = int(num_results_int)
        except ValueError as e:
            print num_results_raw
            print e, 'Failed to decode value'
            return
        search_params = []
        for start in range(0, num_results, 50):
            if start == 0:
                search_params.append(search_item)
            else:
                new_search_item = copy.copy(search_item)
                new_search_item['start'] = str(start)
                search_params.append(new_search_item)
        return [
            FormRequest(
                SEARCH_URL,
                formdata=item,
                dont_filter=True,
                callback=self.parse_items
            ) for item in search_params ]

    def parse_items(self, response):
        """ Get target items for processing """
        for item in response.xpath('//*[@id="tor-tbl"]/tbody/tr[*]/td[4]/div[1]'):
            search_item = SearchItem()
            search_item['title'] = item.xpath('a/text()').extract()[0]
            search_item['link'] = item.xpath('a/@href').extract()[0]
            yield search_item
