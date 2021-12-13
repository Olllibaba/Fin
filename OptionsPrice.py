lala

import requests


#This one works
#page = requests.get("https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/")

url="https://finance.yahoo.com/quote/TSLA/options?p=TSLA&date=1705622400"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
resp = requests.get(url, headers=headers, timeout=5).text
print(resp)

#data = pd.read_html(link)

# function to find Minimum for Ticker + Expiration Date

# project Trajectory
