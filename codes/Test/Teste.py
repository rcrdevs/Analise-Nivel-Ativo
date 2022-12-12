#%%
import pandas as pd
from herepy import *
from herepy import PublicTransitApi, PublicTransitSearchMethod
from herepy import FleetTelematicsApi

places_api = PlacesApi(api_key="KJCpV2lR4eolskhN4je9xDs74WG-hg1soGWJxPX9oHo")
traffic_api = TrafficApi(api_key="KJCpV2lR4eolskhN4je9xDs74WG-hg1soGWJxPX9oHo")

#

resplist = []

response = traffic_api.flow_using_proximity(
    latitude=-8.117328736426977, longitude=-34.9024128585056, distance=0.4
)
resplist.append(response)
#%%
respdict = response.as_dict()
size = len(respdict['RWS'][0]['RW'])

index = 0

while index < size:
    for i in resplist:
        vicinity = (i.as_dict()['RWS'][0]['RW'][index]['FIS'][0]['FI'][0]['TMC']['DE'])
        jamfactor = (i.as_dict()['RWS'][0]['RW'][index]['FIS'][0]['FI'][0]['CF'][0]['JF'])
        index = index + 1

average = jamfactor / size
print(average)

#%%
import requests

resplist2 = []
response = places_api.places_in_circle(
    coordinates=[-19.93616, -43.93242], radius=1000, query="Assaí", limit=5
)

index = 0
size = len(response.as_dict()['items'])

while index < size:
    print(response.as_dict()['items'][index]['title'])
    index = index + 1
#%%

#########################################
from herepy import VectorTileApi, VectorMapTileLayer

vector_tile_api = VectorTileApi(api_key="KJCpV2lR4eolskhN4je9xDs74WG-hg1soGWJxPX9oHo")

# Returns a tile using base layer and other default parameters
vector_tile = vector_tile_api.get_vectortile(
    latitude=52.525439, longitude=13.38727, zoom=12
)
print(vector_tile)

# Returns tile using core layer with other default parameters
vector_tile = vector_tile_api.get_vectortile(
    latitude=52.525439, longitude=13.38727, zoom=12, layer=VectorMapTileLayer.core
)
display(vector_tile)
# %%
