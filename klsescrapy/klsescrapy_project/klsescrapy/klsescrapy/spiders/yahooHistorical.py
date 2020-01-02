# -*- coding: utf-8 -*-
import scrapy
from yahoo_historical import Fetcher
from klsescrapy.extraFunction import ExtraFunction
from bs4 import BeautifulSoup
import re

class YahoohistoricalSpider(scrapy.Spider):
    ticker = "0138" + ".KL"
    name = 'yahooHistorical'
    url = "https://finance.yahoo.com/quote/%s/history" % (ticker)
    api_url = (
        "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=%s&events=%s&crumb=%s"
    )

    custom_settings = {"DOWNLOADER_MIDDLEWARES": { 'klsescrapy.middlewares.KlsescrapyDownloaderMiddleware': None }}
    start_urls = [url]

    def parse(self, response):
        #data = Fetcher(self.ticker, [2007,1,1], [2017,1,1])
        #self.cookie,self.crumb = ExtraFunction(self.ticker).getCrumb()
        #soup = BeautifulSoup(response.text, 'lxml')
        ##print(soup)
        crumb = ExtraFunction(response.text).getCrumb()
        self.log(crumb)
        url2 = "https://query1.finance.yahoo.com/v7/finance/download/0138.KL?period1=1546185600&period2=1577721600&interval=1d&events=history&crumb=%s" %(crumb)
        scrapy.Request(url2)


