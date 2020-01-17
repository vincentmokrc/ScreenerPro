from tkinter import * 
from tkinter.ttk import *
import threading

root = Tk()

def StartDownload():
    import pandas
    import pandas_datareader.data as web
    import datetime
    import time

    df = pandas.read_csv('C://Users//vince//Documents//GitHub//klsescrapy//klsescrapy_project//klsescrapy//companyList_MainMarket.csv',dtype={'Stock Code': object})
    df2 = pandas.read_csv('C://Users//vince//Documents//GitHub//klsescrapy//klsescrapy_project//klsescrapy//companyList_AceMarket.csv',dtype={'Stock Code': object})

    df = df.append(df2)
    symbol = df['Stock Code'].tolist()
    print(symbol)

    today = datetime.datetime.today()
    end = datetime.datetime(today.year,today.month,today.day)
    
    start = datetime.datetime(today.year,today.month,today.day)
    
    #set path for csv file
    path_out = 'c:/python_programs_output/'
    dftoday = web.DataReader("0095.KL", 'yahoo', start, end)

    i=0
    while i<len(symbol):
        try:
            df = web.DataReader(symbol[i] + ".KL", 'yahoo', start, end)
            oridf = pandas.read_csv(path_out + symbol[i] + ".csv",index_col=0)
            oridf.index = pandas.to_datetime(oridf.index)
            result = oridf.tail(1).index == df.tail(1).index
            if(result[0] == False):
                added = oridf.append(df)
                dftoday = df
                added.to_csv(path_out+ symbol[i] +'.csv')
                print (i,symbol[i],'has data stored to csv file')
            else:
                if(oridf.tail(1).index != dftoday.head(1).index):
                    df.index = dftoday.index
                    df['Volume'] = 0
                    added = oridf.append(df)
                    added.to_csv(path_out+ symbol[i] +'.csv')
                    print (i,symbol[i],'has Vol 0 data fill to csv file')
                else:
                    print (i,symbol[i],'data available file')
        except:
            try:
                newdf = oridf.tail(1)
                newdf.index = dftoday.index
                newdf['Volume'] = 0
                newdf['Low'] = newdf['High'] = newdf['Adj Close'] = newdf['Open'] = newdf['Close']
                result2 = oridf.tail(1).index == dftoday.index
                print(result2)
                if(result2[0] == False):
                    added = oridf.append(newdf)
                    added.to_csv(path_out+ symbol[i] +'.csv')
                    print("Force information for ticker # and symbol:")
                    print (i,symbol[i])
                else:
                    print (i,symbol[i],'data available file 2')
            except:
                print("No information for ticker # and symbol:")
                print (i,symbol[i])
                pass
        i = i+1

Button(root, text = 'Start Download', command = StartDownload).pack(pady = 10) 

root.mainloop()
