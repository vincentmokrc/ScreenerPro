import calendar as cal
import datetime as dt
import re
import time
import warnings

import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup

class ExtraFunction:
    def __init__(self, inresponse):
        self.inresponse = inresponse

    def getCrumb(self):
        soup = BeautifulSoup(self.inresponse, 'lxml')
        crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(soup))
        #url = "https://finance.yahoo.com/quote/%s/history" % (self.ticker)
        #r = requests.get(url)
        #txt = r.content
        #cookie = r.cookies["B"]
        #pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')

        #for line in txt.splitlines():
        #    m = pattern.match(line.decode("utf-8"))
        #    if m is not None:
        #        crumb = m.groupdict()["crumb"]
        #        crumb = crumb.replace(u"\\u002F", "/")
        return crumb  # return a tuple of crumb and cookie
