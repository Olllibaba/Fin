
import re
s='{“contractSymbol":"TSLA240119C00010000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":10,"fmt":"10.00"},"contractSize":"REGULAR","lastPrice":{"raw":1067.8,"fmt":"1,067.80"},"inTheMoney":true,"openInterest":{"raw":22,"fmt":"22","longFmt":"22"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1018.5,"fmt":"1,018.50"},"volume":{"raw":10,"fmt":"10","longFmt":"10"},"lastTradeDate":{"raw":1636577725,"fmt":"2021-11-10","longFmt":"2021-11-10T20:55"},"bid":{"raw":998.5,"fmt":"998.50"}},{“contractSymbol":"TSLA240119C00015000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":15,"fmt":"15.00"},"contractSize":"REGULAR","lastPrice":{"raw":1060.5,"fmt":"1,060.50"},"inTheMoney":true,"openInterest":{"raw":45,"fmt":"45","longFmt":"45"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1013.5,"fmt":"1,013.50"},"volume":{"raw":43,"fmt":"43","longFmt":"43"},"lastTradeDate":{"raw":1636577609,"fmt":"2021-11-10","longFmt":"2021-11-10T20:53"},"bid"'
#s='{“contractSymbol":"TSLA240119C00010000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":10,"fmt":"10.00"},"contractSize":"REGULAR","lastPrice":{"raw":1067.8,"fmt":"1,067.80"},"inTheMoney":true,"openInterest":{"raw":22,"fmt":"22","longFmt":"22"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1018.5,"fmt":"1,018.50"},"volume":{"raw":10,"fmt":"10","longFmt":"10"},"lastTradeDate":{"raw":1636577725,"fmt":"2021-11-10","longFmt":"2021-11-10T20:55"},"bid":{"raw":998.5,"fmt":"998.50"}},{"contractSymbol":"TSLA240119C00015000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":15,"fmt":"15.00"},"contractSize":"REGULAR","lastPrice":{"raw":1060.5,"fmt":"1,060.50"},"inTheMoney":true,"openInterest":{"raw":45,"fmt":"45","longFmt":"45"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1013.5,"fmt":"1,013.50"},"volume":{"raw":43,"fmt":"43","longFmt":"43"},"lastTradeDate":{"raw":1636577609,"fmt":"2021-11-10","longFmt":"2021-11-10T20:53"},"bid"'
#s='“contractSymbol"1"bid"“contractSymbol"2"bid"“contractSymbol"3"bid"“contractSymbol"1"bid"'

print(s)

d=re.findall('“contractSymbol"(.*?)"bid"',s)
print(d)
print('NEXT NEXT')
print(d[1])


#s= '{“contractSymbol":"TSLA240119C00010000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":10,"fmt":"10.00"},"contractSize":"REGULAR","lastPrice":{"raw":1067.8,"fmt":"1,067.80"},"inTheMoney":true,"openInterest":{"raw":22,"fmt":"22","longFmt":"22"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1018.5,"fmt":"1,018.50"},"volume":{"raw":10,"fmt":"10","longFmt":"10"},"lastTradeDate":{"raw":1636577725,"fmt":"2021-11-10","longFmt":"2021-11-10T20:55"},"bid":{"raw":998.5,"fmt":"998.50"}},{"contractSymbol":"TSLA240119C00015000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":15,"fmt":"15.00"},"contractSize":"REGULAR","lastPrice":{"raw":1060.5,"fmt":"1,060.50"},"inTheMoney":true,"openInterest":{"raw":45,"fmt":"45","longFmt":"45"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1013.5,"fmt":"1,013.50"},"volume":{"raw":43,"fmt":"43","longFmt":"43"},"lastTradeDate":{"raw":1636577609,"fmt":"2021-11-10","longFmt":"2021-11-10T20:53"},"bid":{"raw":994,"fmt":"994.00"}},{"contractSymbol":"TSLA240119C00020000","impliedVolatility":{"raw":0,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":20,"fmt":"20.00"},"contractSize":"REGULAR","lastPrice":{"raw":1046.2,"fmt":"1,046.20"},"inTheMoney":true,"openInterest":{"raw":21,"fmt":"21","longFmt":"21"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1009,"fmt":"1,009.00"},"volume":{"raw":36,"fmt":"36","longFmt":"36"},"lastTradeDate":{"raw":1636577277,"fmt":"2021-11-10","longFmt":"2021-11-10T20:47"},"bid":{"raw":989,"fmt":"989.00"}},{"contractSymbol":"TSLA240119C00025000","impliedVolatility":{"raw":0.000010000000000000003,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":25,"fmt":"25.00"},"contractSize":"REGULAR","lastPrice":{"raw":1139.49,"fmt":"1,139.49"},"inTheMoney":true,"openInterest":'
#print(s)
#print('NEXT NEXT')
#d=re.findall('“contractSymbol"(.*?)"bid"',s)
#print(d)