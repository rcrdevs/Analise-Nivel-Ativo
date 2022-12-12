#%%
import pandas as pd
import folium  
from folium import plugins

#maplog = pd.read_excel(name + '.xlsx')
#maplog = pd.read_excel('output.xlsx', sheet_name='Posto')


api_key = 'HERE_API_KEY.txt'
maplog = 'https://1.traffic.maps.ls.hereapi.com/maptile/2.1/traffictile/newest/normal.day/13/4358/2842/512/png?apiKey={api_key}&ppi=500&time=2021-09-13T16:00:00z'

display(maplog)
#%%

coordenadas=[]
for lat, lng in zip(maplog.Latitude.values, maplog.Longitude.values):
    coordenadas.append([lat,lng])

map = folium.Map(location= [-23.58097625684886, -46.68024668040564],tiles = 'Stamen Terrain', zoom_start=13)
folium.Marker([-23.58097625684886, -46.68024668040564]).add_to(map)

map.add_child(plugins.HeatMap(coordenadas))
map.save('HeatMap.html')

 # %%
