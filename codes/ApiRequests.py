##########################################################CODE 1 - GOOGLE API REQUESTS############################################
#%%
#Imports
import geopy
from distutils.log import info
import time
from tracemalloc import stop
from types import coroutine
import googlemaps
import pandas as pd
from bs4 import BeautifulSoup as BS

#Def kms to meters
def kms_to_meters(kms):
    try:
        return kms * 1_000
    except:
        return 0

#API Key import and inicialization        
API_KEY = 'AIzaSyDYDmvj32u6j6RF4sPv0WCBWMf5XH7iJHI'
map_client = googlemaps.Client(API_KEY)


#Code-start, Adress search, Inputs
addressinp1 = (input("Digite o nome da Rua: "))
addressinp2 = (input("Digite o bairro: "))
addressinp3 = (input("Digite o municipio: "))
address = (addressinp1 + " " + addressinp2 + " " + addressinp3)
escope1 = (input("Digite o primeiro estabelecimento a ser procurado: "))
escope2 = (input("Digite o segundo estabelecimento a ser procurado: "))
escope3 = (input("Digite o terceiro estabelecimento a ser procurado: "))
distanceinp = (input("Digite o perimetro que os estabelecimentos devem ser procurados(Em Kilometros): "))
outinputs = ("Você deseja procurar :", escope1,",", escope2,"e", escope3, "num raio de", distanceinp, "kilometros do endereço", address, "?")

#Sentence slice for output
sentence = ""

for word in outinputs:
    sentence += str(word) + " "

outinputs = (input(sentence))

geocode = map_client.geocode(address=address)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

#Escope 1 Search
search_string = escope1
distance = kms_to_meters(int(distanceinp))
business_list = []

response1 = map_client.places_nearby(
    location=(lat, lng),
    keyword=search_string,
    radius=distance
)   
business_list.extend(response1.get('results'))
next_page_token = response1.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response1 = map_client.places_nearby(
        location=(lat, lng),
        keyword=search_string,
        radius=distance,
        page_token=next_page_token
    )
    business_list.extend(response1.get('results'))
    next_page_token = response1.get('next_page_token')
escope1_list= (business_list[0:5])

#Slice Lat and Lng - Escope 1
latshoppinglist = []
lngshoppinglist = []
respshopping = escope1_list
listsize = len(escope1_list)

for i in range(len(respshopping)):
    while i < listsize:
        latshopping = (respshopping[i]['geometry']['location'].get ('lat'))
        lngshopping = (respshopping[i]['geometry']['location'].get ('lng'))
        i = i + 1
        latshoppinglist.append(latshopping)
        lngshoppinglist.append(lngshopping)


lat1 = (latshoppinglist[0:listsize])
lng1 = (lngshoppinglist[0:listsize])
#Dataframe save structure - Escope 1
time.sleep(6)
df = pd.DataFrame(escope1_list)
dfcol = df.columns

for i in dfcol:
    if i == 'place_id':
        df['Url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
    else:
        continue

df['Latitude'] = lat1
df['Longitude'] = lng1

##Escope 2 Start
search_string = escope2
distance = kms_to_meters(int(distanceinp))
business_list = []

response2 = map_client.places_nearby(
    location=(lat, lng),
    keyword=search_string,
    radius=distance + 5
)   

business_list.extend(response2.get('results'))
next_page_token = response2.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response2 = map_client.places_nearby(
        location=(lat, lng),
        keyword=search_string,
        radius=distance,
        page_token=next_page_token
    ) 
    business_list.extend(response2.get('results'))
    next_page_token = response2.get('next_page_token')
mercado_list= (business_list[0:5])

#Slice Lat and Lng - Escope 2
latshoppinglist = []
lngshoppinglist = []
respshopping = mercado_list
listsize = len(respshopping)

for i in range(len(respshopping)):
    while i < listsize:
        latshopping = (respshopping[i]['geometry']['location'].get ('lat'))
        lngshopping = (respshopping[i]['geometry']['location'].get ('lng'))
        i = i + 1
        latshoppinglist.append(latshopping)
        lngshoppinglist.append(lngshopping)


lat2 = (latshoppinglist[0:listsize])
lng2 = (lngshoppinglist[0:listsize])

#Dataframe 2 Save Estructure
time.sleep(6)
df2 = pd.DataFrame(mercado_list)
df2col = df2.columns
for i in df2col:
    if i == 'place_id':
        df2['Url'] = 'https://www.google.com/maps/place/?q=place_id:' + df2['place_id']
    else:
        continue

df2['Latitude'] = lat2
df2['Longitude'] = lng2
##
##Escope 3 Start
escope = (escope3)
search_string = escope
distance = kms_to_meters(int(distanceinp))
business_list = []


response3 = map_client.places_nearby(
    location=(lat, lng),
    keyword=search_string,
    radius=distance
)   

business_list.extend(response3.get('results'))
next_page_token = response3.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response3 = map_client.places_nearby(
        location=(lat, lng),
        keyword=search_string,
        radius=distance,
        page_token=next_page_token
    )   
    business_list.extend(response3.get('results'))
    next_page_token = response3.get('next_page_token')
metro_list= (business_list[0:5])

#Slice Lat and Lng
latshoppinglist = []
lngshoppinglist = []
respshopping = metro_list
listsize = len(respshopping)

for i in range(len(respshopping)):
    while i < listsize:
        latshopping = (respshopping[i]['geometry']['location'].get ('lat'))
        lngshopping = (respshopping[i]['geometry']['location'].get ('lng'))
        i = i + 1
        latshoppinglist.append(latshopping)
        lngshoppinglist.append(lngshopping)


lat3 = (latshoppinglist[0:listsize])
lng3 = (lngshoppinglist[0:listsize])

#Dataframe 3 Save Estructure
#%%
time.sleep(6)
df3 = pd.DataFrame(metro_list)
df3col = df3.columns

for i in df3col:
    if i == 'place_id':
        df3['Url'] = 'https://www.google.com/maps/place/?q=place_id:' + df3['place_id']
    else:
        continue

df3['Latitude'] = lat3
df3['Longitude'] = lng3

display(df3)
#%%

###Strings das infos do endereço de referencia
geo2 = geopy.geocoders.Nominatim(user_agent="Intro Geocode").reverse(str(lat) + ", " + str(lng))

geo2 = str(geo2).split(',')

index = -1
listsize = len(geo2)
df4list = []
df4link = pd.DataFrame(geocode)
df4col = df4link.columns


for i in df4col:
    if i == 'place_id':
        link = 'https://www.google.com/maps/place/?q=place_id:' + df4link['place_id']
    else:
        continue


while listsize -1 > index:
    index = index + 1
    df4list.append(geo2[index])

df4list.append(link)
#%%

df0 = pd.DataFrame(columns = df4list)
#%%
# Drops

#dfdict = ['name', 'business_status', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon']
#df2col = df2.columns

#for i in dfdict:
#    for j in df2col:
#        if i == j:
#            df2.columns.drop(i)
#    else:
#        continue


#for i in df2:
#    print(i)
#%%

df.drop(['geometry', 'business_status', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)
df2.drop(['geometry', 'business_status', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)
df3.drop(['geometry', 'business_status', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)

#Append Dataframes into xlsx sheets
name = input('Digite o nome do arquivo :')
with pd.ExcelWriter (name + '.xlsx') as writer:
    df0.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    df.to_excel(writer, sheet_name=escope1, index = False)
    df2.to_excel(writer, sheet_name=escope2, index = False)
    df3.to_excel(writer, sheet_name=escope3, index = False) 
time.sleep(2)
################################################# END CODE 1 ##############################################################
# %%
