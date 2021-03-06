

import requests
import numpy as np
import re
#import pandas as pd



#Define Function that takes Ticker Symbol and returns a List of URLs
def TickUrl(ticker):

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
    date=np.float_(expDates)

    return urls

#Define function that takes URL and returns Expiration date as a 10-digit number, STILL AS STRING, CONVERT TO GOOD DATE
def expDate(url):
    return [url[x][-10:] for x in range(len(url))]

#Define Function that takes Yahoo Finance URL and returns Options Data as Matrix
#Colums: C1:Call(+1)/Put(-1) C2:Strike C3:LastPrice C4:Change C5:Bid C6:Ask C7:OpenInterest C8:Volume C9:IV
def OptData(url):
#You need to pretend to be a user unless Yahoo will block you, not sure how the following lines actually work
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    resp = requests.get(url, headers=headers, timeout=15).text
#Vectorize Data
    d=re.findall('contractSymbol"(.*?)"}},{"',resp)
#Problem 1: The first entry has to be removed, it doesn't carry any information
    del d[0]
#Problem 2: The Data is here twice
    del d[len(d)//2:]

#Build Data Matrix A  Colum 1: Call(+1)/Put(-1) C2: Strike C3: Last Price  C4: Change C5: Bid C6:Ask C7:OpenInterest C8:Volume C9:IV
    A = np.zeros((len(d), 9))
# C1: Call or Put
    end = [x.find('","impliedVolatility') for x in d]
    CoP = [d[x][end[x]-9:end[x]-8] for x in range(len(d))]
    CoP = ['-1' if CoP[i]=='P' else '1' for i in range(len(d))]
    A[:,0] = np.float_(CoP)
# C2: Strike Price
    strikes= [d[x][end[x]-8:end[x]] for x in range(len(d))]
    A[:,1] = np.float_(strikes)/1000
# C3: Last Price
    end = [x.find('"lastPrice":{"raw":') for x in d]
    Price = [d[x][end[x]+19:end[x]+26] for x in range(len(d))]
    Price = [re.sub("[^0-9.]", "",Price[x]) for x in range(len(d))]
    A[:,2] = np.float_(Price)

# C4: Change in Price
    end = [x.find('"change":{"raw"') for x in d]
    CPrice = [d[x][end[x]+16:end[x]+24] for x in range(len(d))]
    CPrice = [re.sub("[^0-9.]", "",CPrice[x]) for x in range(len(d))]
    A[:,3] = np.float_(CPrice)

# C5: Bid
    end = [x.find('"bid":{"raw":') for x in d]
    Bid = [d[x][end[x]+13:end[x]+22] for x in range(len(d))]
    Bid = [re.sub("[^0-9.]", "",Bid[x]) for x in range(len(d))]
    A[:,4] = np.float_(Bid)

# C6:Ask
    end = [x.find('"ask":{"raw":') for x in d]
    Ask = [d[x][end[x]+13:end[x]+22] for x in range(len(d))]
    Ask = [re.sub("[^0-9.]", "",Ask[x]) for x in range(len(d))]
    A[:,5] = np.float_(Ask)

#C7:OpenInterest
    end = [x.find('"openInterest":{"raw":') for x in d]
    OI = [d[x][end[x]+22:end[x]+30] for x in range(len(d))]
    OI = [re.sub("[^0-9.]", "",OI[x]) for x in range(len(d))]
    OI = [OI[x] if len(OI[x])>0 else '0' for x in range(len(d))]
    A[:,6] = np.float_(OI)

#C8:Volume
    end = [x.find('"volume":{"raw":') for x in d]
    Vol = [d[x][end[x]+16:end[x]+23] for x in range(len(d))]
    Vol = [re.sub("[^0-9.]", "",Vol[x]) for x in range(len(d))]
    A[:,7] = np.float_(Vol)

#C9: IV
    end = [x.find('"impliedVolatility":{"raw":') for x in d]
    IV = [d[x][end[x]+27:end[x]+35] for x in range(len(d))]
    IV = [re.sub("[^0-9.]", "",IV[x]) for x in range(len(d))]
    A[:,8] = np.float_(IV)

#End
    return A

#Define FUnction that takes OptData and a hypothetical Strike Price and returns the Payout in Billions
def Payout(StockPrice,data):
    Payout = [100 * (StockPrice - data[n, 1]) * data[n, 0] * data[n, 6] for n in range(len(data))]
    Payout = [Payout[n] if Payout[n] >= 0 else 0 for n in range(len(Payout))]
    Payout = np.sum(Payout)
    return Payout/1000000

#Define Function that takes predicts the Payout given the Extracted Options Data
def PricePredict(data):
    prices = range(int(data[0, 1]), int(data[len(data) - 1, 1]), 1)
    Pay = [Payout(x, data) for x in prices]
    PredPrice = prices[Pay.index(min(Pay))]
    return PredPrice


#Small D Approach
#ticker='amzn'
#urls=TickUrl(ticker)
#Data=OptData(urls[1])
#Prediction = PricePredict(Data)
#print(Prediction)



#BIG D Approach
ticker='aapl'
urls=TickUrl((ticker))
Data=[OptData(urls[k]) for k in range(len(urls)-1)]
print(len(Data))
Prediction = [PricePredict(Data[k]) for k in range(len(Data)-1)]
print(Prediction)













# Minimize Total Payout as a function of x

# If you want get data for several strikes you have to do this, not really sure why
#ticker='lmt'
#urls=TickUrl(ticker)
#Data=[OptData(urls[k]) for k in [0, len(urls)-1]]
#print(Data)
#print(urls)
#print(expDate(TickUrl(ticker)))























# function to find Minimum for Ticker + Expiration Date

# project Trajectory
