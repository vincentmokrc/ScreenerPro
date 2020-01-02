import pandas
import pandas_datareader.data as web
import datetime

df = pandas.read_csv('C://Users//vince//Documents//GitHub//klsescrapy//klsescrapy_project//klsescrapy//companyList_MainMarket.csv',dtype={'Stock Code': object})


symbol = df['Stock Code'].tolist()
print(symbol)


end = datetime.datetime.today()
 
start = datetime.date(end.year-5,1,1)
 
#set path for csv file
path_out = 'c:/python_programs_output/'

i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i] + ".KL", 'yahoo', start, end)
        df.to_csv(path_out+ symbol[i] +'.csv')
        print (i, symbol[i],'has data stored to csv file')
    except:
        print("No information for ticker # and symbol:")
        print (i,symbol[i])
        pass
    i = i+1
