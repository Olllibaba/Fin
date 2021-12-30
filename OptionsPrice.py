

import requests
import numpy as np
import re
import pandas as pd


#Get data(called resp) from Yahoo
url="https://finance.yahoo.com/quote/TSLA/options?p=TSLA&date=1705622400"
url="https://finance.yahoo.com/quote/AAPL/options?p=AAPL&date=1705622400"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
resp = requests.get(url, headers=headers, timeout=5).text

#Vectorize Data
d=re.findall('contractSymbol"(.*?)"}},{"',resp)

#This is how the raw data looks like:
#:"TSLA240119C00005000",
# "impliedVolatility":{"raw":2.6611361596679695,"fmt":"266.11%"},
# "expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},
# "change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":5,"fmt":"5.00"},
# "contractSize":"REGULAR","lastPrice":{"raw":1066.82,"fmt":"1,066.82"},# "inTheMoney":true,
# "openInterest":{"raw":315,"fmt":"315","longFmt":"315"},
# "percentChange":{"raw":0,"fmt":"0.00%"},
# "ask":{"raw":1075,"fmt":"1,075.00"},
# "volume":{"raw":1,"fmt":"1","longFmt":"1"},
# "lastTradeDate":{"raw":1638987799,"fmt":"2021-12-08",
# "longFmt":"2021-12-08T18:23"},
# "bid":{"raw":1055,"fmt":"1,055.00

#Problem 1: The first entry has to be removed, it doesn't carry any information
del d[0]

# PROBLEM 2: The Data is here twice
del d[len(d)//2:]

    # PROBLEM 3: Some Strikes only exist for put or call BUT Does Not Matter, Data is Data    # Idea: Identify the singles and remove them #get strike before implied volaitily

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

print(A)

a













# function to find Minimum for Ticker + Expiration Date

# project Trajectory
