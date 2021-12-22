

import requests
import numpy as np



#Get data(called resp) from Yahoo
url="https://finance.yahoo.com/quote/TSLA/options?p=TSLA&date=1705622400"
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
print(A)

#Get Call Data


start = resp.find('"contractSymbol":"') + 10
end = resp.find('"bid":{"raw":0,"fmt":"0.00"}}', start)
call_data = resp[start:end]
print(call_data)
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
