

import requests
import numpy as np
import re
import pandas as pd


#Get data(called resp) from Yahoo
url="https://finance.yahoo.com/quote/TSLA/options?p=TSLA&date=1705622400"
#url="https://finance.yahoo.com/quote/AAPL/options?p=AAPL&date=1705622400"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
resp = requests.get(url, headers=headers, timeout=5).text
#print(resp)


#Get Strikes and define Storage Matrix data
start = resp.find('"strikes":') + 11
end = resp.find('],"underlyingSymbol"', start)
strikes = resp[start:end]
strikes = strikes.split(",")
strikes = np.float_(strikes)
#print(strikes)
#print(strikes[0]+strikes[1])

#Build Data Matrix A
A = np.zeros((len(strikes), 10))
    #First Row is Strike Prize
A[:,0] = strikes
print(len(strikes))
#print(A)

#Vectorize Data

d=re.findall('contractSymbol"(.*?)"bid',resp)

#That is the raw data, looks like this:   -more entires than strikes(==>extraction not perfect)

# :"TSLA240119C00020000","impliedVolatility":{"raw":2.182621730957031,"fmt":"218.26%"},
# "expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},
# "change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":20,"fmt":"20.00"},
# "contractSize":"REGULAR","lastPrice":{"raw":1046.2,"fmt":"1,046.20"},
# "inTheMoney":true,"openInterest":{"raw":21,"fmt":"21","longFmt":"21"},
# "percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1009,"fmt":"1,009.00"},
# "volume":{"raw":36,"fmt":"36","longFmt":"36"},"lastTradeDate":{"raw":1636577277,"fmt":"2021-11-10","longFmt":"2021-11-10T20:47"},

#Cut Data (only all strikes)
del d[0]

#print(d[3][0:25])


#a=d.str[:25]
#print('New Line')

#print(len(d))

#call_data = np.zeros((len(strikes), 5))


    #Last PRice
    #Bid
    #Ask
    #Change
    #Volume
    #Open Interest



#Build Call Data


#Extract String after contractSymbol":"TSLA...DATE...C0000(?)STRIKE         TO      next contract Symbol
#Parse Data ==> Vector with Call Strikes and Data


#Build Put Data




# function to find Minimum for Ticker + Expiration Date

# project Trajectory
