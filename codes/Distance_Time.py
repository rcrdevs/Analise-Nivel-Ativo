#%%
# Importing googlemaps module
import googlemaps
import pandas as pd
from bs4 import BeautifulSoup as BS
from ApiRequests import *
from ApiRequests import name

# Requires API key
gmaps = googlemaps.Client(key=API_KEY)
# Sources
source = address
destShopping = pd.read_excel(name + '.xlsx', sheet_name=escope1)
destMercado = pd.read_excel(name + '.xlsx', sheet_name=escope2)
destInfra = pd.read_excel(name + '.xlsx', sheet_name=escope3)
addr1 = destShopping['vicinity']
addr2 = destMercado['vicinity']
addr3 = destInfra['vicinity']
actual_distance_escope1 = []
actual_distance_escope2 = []
actual_distance_escope3 = []
time_escope1 = []
time_escope2 = []
time_escope3 = []
index = 0

# While Escope 1
listsize = len(addr1)

while index < listsize:
    my_dist = gmaps.distance_matrix(source, addr1[index], mode= 'driving')["rows"][0]["elements"][0]["distance"]["text"]
    my_dist_time = gmaps.distance_matrix(source, addr1[index], mode= 'driving') ["rows"][0]["elements"][0]["duration"]["text"]
    actual_distance_escope1.append(my_dist)
    time_escope1.append(my_dist_time)
    index = index + 1

# While Escope 2
index = 0
listsize = len(addr2)

while index < listsize:
    my_dist = gmaps.distance_matrix(source, addr2[index], mode= 'driving')["rows"][0]["elements"][0]["distance"]["text"]
    my_dist_time = gmaps.distance_matrix(source, addr2[index], mode= 'driving') ["rows"][0]["elements"][0]["duration"]["text"]
    actual_distance_escope2.append(my_dist)
    time_escope2.append(my_dist_time)
    index = index + 1

# While Escope 3
index = 0
listsize = len(addr3)

while index < listsize:
    my_dist = gmaps.distance_matrix(source, addr3[index], mode= 'driving')["rows"][0]["elements"][0]["distance"]["text"]
    my_dist_time = gmaps.distance_matrix(source, addr3[index], mode= 'driving') ["rows"][0]["elements"][0]["duration"]["text"]
    actual_distance_escope3.append(my_dist)
    time_escope3.append(my_dist_time)
    index = index + 1

#%%
# DF Escope 1
df['Distance'] = actual_distance_escope1
df['Time'] = time_escope1

# DF Escope 2
df2['Distance'] = actual_distance_escope2
df2['Time'] = time_escope2

# DF Escope 3
df3['Distance'] = actual_distance_escope3
df3['Time'] = time_escope3
#%%