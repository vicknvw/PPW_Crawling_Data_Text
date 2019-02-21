# -*- coding: utf-8 -*-
import scrapy


class CrawlingSpider(scrapy.Spider):
    name = 'crawling'
    allowed_domains = ['www.disney.id']
    start_urls = ['http://www.disney.id/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.title p ::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
