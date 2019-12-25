import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import Info.url as URL
import selenium.webdriver.support.select

class getList:

    @staticmethod
    def companyList(market_url):
        url_is = URL.listing_directory + market_url
        driver = webdriver.Firefox()
        driver.get(url_is)
        result_soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = result_soup.find('table', id="DataTables_Table_0")
        table_rows = table.find_all('tr')

        res = []
        for tr in table_rows:
            td = tr.find_all('td')
            td2 = tr.find_all('td')[1:2]
            for d in td2: 
                 a = d.find_all('a', href=True)
                 for b in a:
                    code=b['href'].split('stock_code=')[1]
                    print(code)
            
            row = [d.text.strip() for d in td]
            row.append(code)
            if row:
                res.append(row)

        df = pd.DataFrame(res, columns=["No","Company Name", "Company Website","Code"])
        return df[1:]