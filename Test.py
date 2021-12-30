import numpy as np
import re

s='{"contractSymbol":"TSLA240119C00065000","impliedVolatility":{"raw":0.000010000000000000003,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":65,"fmt":"65.00"},"contractSize":"REGULAR","lastPrice":{"raw":1010,"fmt":"1,010.00"},"inTheMoney":true,"openInterest":{"raw":23,"fmt":"23","longFmt":"23"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":966,"fmt":"966.00"},"volume":{"raw":132,"fmt":"132","longFmt":"132"},"lastTradeDate":{"raw":1636577686,"fmt":"2021-11-10","longFmt":"2021-11-10T20:54"},"bid":{"raw":946,"fmt":"946.00"}},{"contractSymbol":"TSLA240119C00070000","impliedVolatility":{"raw":1.143436900024414,"fmt":"114.34%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":70,"fmt":"70.00"},"contractSize":"REGULAR","lastPrice":{"raw":1060.52,"fmt":"1,060.52"},"inTheMoney":true,"openInterest":{"raw":20,"fmt":"20","longFmt":"20"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":1016.5,"fmt":"1,016.50"},"volume":{"raw":5,"fmt":"5","longFmt":"5"},"lastTradeDate":{"raw":1638206162,"fmt":"2021-11-29","longFmt":"2021-11-29T17:16"},"bid":{"raw":997,"fmt":"997.00"}},{"contractSymbol":"TSLA240119C00075000","impliedVolatility":{"raw":0.000010000000000000003,"fmt":"0.00%"},"expiration":{"raw":1705622400,"fmt":"2024-01-19","longFmt":"2024-01-19T00:00"},"change":{"raw":0,"fmt":"0.00"},"currency":"USD","strike":{"raw":75,"fmt":"75.00"},"contractSize":"REGULAR","lastPrice":{"raw":988.8,"fmt":"988.80"},"inTheMoney":true,"openInterest":{"raw":4,"fmt":"4","longFmt":"4"},"percentChange":{"raw":0,"fmt":"0.00%"},"ask":{"raw":956.5,"fmt":"956.50"},"volume":{"raw":2,"fmt":"2","longFmt":"2"},"lastTradeDate":{"raw":1636663057,"fmt":"2021-11-11","longFmt":"2021-11-11T20:37"},"bid":{"raw":936.5,"fmt":"936.50"}},{"contractSymbol":"TSLA240119C00080000","impliedVolatility":'


d=re.findall('contractSymbol"(.*?)"bid',s)
d=re.findall('contractSymbol"(.*?)"}},{"',s)
print(len(d))

print('lala')
print(s[1])

