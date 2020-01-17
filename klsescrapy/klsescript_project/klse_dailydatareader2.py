import pandas
import pandas_datareader.data as web
import datetime

df = pandas.read_csv('C://Users//vince//Documents//GitHub//klsescrapy//klsescrapy_project//klsescrapy//companyList_MainMarket.csv',dtype={'Stock Code': object})
df2 = pandas.read_csv('C://Users//vince//Documents//GitHub//klsescrapy//klsescrapy_project//klsescrapy//companyList_AceMarket.csv',dtype={'Stock Code': object})

df = df.append(df2)
symbol = df['Stock Code'].tolist()
print(symbol)

end = datetime.datetime(2020,1,3)
start = datetime.datetime(2020,1,3)
#set path for csv file
path_out = 'c:/python_programs_output/'
dftoday = web.DataReader("0095.KL", 'yahoo', start, end)

i=0
while i<len(symbol):
    for k in range(3):
        try:
            df = web.DataReader(symbol[i] + ".KL", 'yahoo', start, end)
            oridf = pandas.read_csv(path_out + symbol[i] + ".csv",index_col=0)
            oridf.index = pandas.to_datetime(oridf.index)
            result = oridf.tail(1).index == df.tail(1).index
            if(result[0] == False):
                added = oridf.append(df)
                added.to_csv(path_out+ symbol[i] +'.csv')
                print (i,symbol[i],'has data stored to csv file')
                break
            else:
                if(k == 1 and oridf.tail(1).index != dftoday.head(1).index):
                    df.index = dftoday.index
                    df['Volume'] = 0
                    added = oridf.append(df)
                    added.to_csv(path_out+ symbol[i] +'.csv')
                    print (i,symbol[i],'has Vol 0 data fill to csv file')
                    break
                else:
                    print (i,symbol[i],'data available file')
        except:
            print("No information for ticker # and symbol:")
            print (i,symbol[i])
            pass
    i = i+1