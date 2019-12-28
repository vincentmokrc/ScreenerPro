# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from w3lib.html import remove_tags


class BasicSpider(scrapy.Spider):
    name = 'basic'
    start_urls = ['https://www.bursamalaysia.com/trade/trading_resources/listing_directory/ace_market']

    def parse(self, response):
        #streamer = response.xpath('//table[@id = "DataTables_Table_0"]/tbody/tr/td[]/text()').extract()
        
        #self.log(response.xpath('//table[@id = "DataTables_Table_0"]//td[1]//text()').extract())
        companyStockCode = response.xpath('//table[@id = "DataTables_Table_0"]//td[2]//a//@href').re('stock_code=(.*)')
        companyName = response.xpath('//table[@id = "DataTables_Table_0"]//td[2]//a//text()').extract()
        companyURL = response.xpath('//table[@id = "DataTables_Table_0"]//td[3]//a//@href').extract()
        self.log(len(companyStockCode))
        self.log(len(companyURL))

        length = len(companyStockCode)
        for i in range(length):
            companyStockCode[i] = str(companyStockCode[i]).zfill(4)
        
        
        company_list = pd.DataFrame(
            {
                'Stock Code' : companyStockCode,
                'Company Name' : companyName,
                'URL' : companyURL
            }
        )
        company_list.to_csv('companyList.csv',index=False)
        