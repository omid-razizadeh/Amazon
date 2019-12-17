# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 3
    start_urls = [
        'https://www.amazon.com/s?rh=n%3A16310101%2Cn%3A%2116310211%2Cn%3A16310231%2Cn%3A16521305011%2Cn%3A16318401%2Cn%3A16318511&page=2&qid=1576118084&ref=lp_16318511_pg_2'
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('span.a-size-base-plus.a-color-base.a-text-normal::text').extract()
        product_price1 = response.css('span.a-price > span.a-offscreen').css('::text').extract()
        product_price = list(filter(('price').__ne__, product_price1))

        items['product_name']=product_name
        items['product_price']=product_price


        yield items

        next_page = 'https://www.amazon.com/s?i=grocery&rh=n%3A16310101%2Cn%3A16310211%2Cn%3A16310231%2Cn%3A16521305011%2Cn%3A16318401%2Cn%3A16318511&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1576114939&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 8:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
