#%%
# -*- coding: utf-8 -*-


import pandas
import collections
import bovespaparser.bovespaparser as bvparser


class CotahistImporter(object):

    def __init__(self, f):
        self.dataFrameMap = {}

        dataMap = collections.defaultdict(list)
        mapping = [("open", 1), ("high", 2), ("low", 3), ("close", 4), ("volume", 5)]

        for symbol, datetime, openv, minv, maxv, close, volume in bvparser.parsedata(f):
            symbolData = dataMap.get(symbol)
            symbolData.append([datetime, openv, maxv, minv, close, volume])

        for symbol in dataMap.keys():
            dataMap.get(symbol).sort()
            data = zip(*dataMap.get(symbol))
            timeseries = dict((column_name, pandas.TimeSeries(data[column_index], index=data[0], name=column_name)) for column_name, column_index in mapping)
            self.dataFrameMap[symbol] = pandas.DataFrame(timeseries, columns=['open', 'high', 'low', 'close', 'volume'])

    def getDataFrameMap(self):
        return self.dataFrameMap
# %%
with open('COTAHIST_A2022.TXT', 'rU') as f:
	result = bvparser.parsedata(f)

print (result)
# %%
import pandas as pd

df = pd.DataFrame(result)
# %%
ticker = 'NEWL11'
for i in df:
    if ticker == i:
        print(i)
# %%
df.loc(df.isin['NEWL11'])
# %%
