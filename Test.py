import numpy as np
import re
import requests
import pandas
#def TickUrl(ticker):
ticker='AAPL'
url='https://finance.yahoo.com/quote/'+ticker+ '/options'

#You need to pretend to be a user unless Yahoo will block you, not sure how the following lines actually work
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
resp = requests.get(url, headers=headers, timeout=5).text
#{"expirationDates":[1641513600,1642118400,1642723200,1643328000,1643932800,1644537600,
# 1645142400,1647561600,1649894400,1653004800,1655424000,1657843200,1663286400,1674172800,1679011200,
# 1686873600,1705622400],"hasMiniOptions":false,"
expDates=re.findall('{"expirationDates":(.*?),"hasMiniOptions"',resp)
expDates=expDates[0]
expDates=expDates[1:len(expDates)-1]
expDates=expDates.split(",")
urls=[url+'?date='+expDates[k] for k in range(len(expDates))]
expDates=np.float_(expDates)
print(expDates)
#print(expDates)
#print(urls)


#es soll auch die time stamp herausgegegben werden
    #return urls




a