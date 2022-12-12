##########################################################CODE 1 - GOOGLE API REQUESTS############################################
#%%
#Imports
from a_dicts import *
import geopy
import time
import googlemaps
import pandas as pd
from bs4 import BeautifulSoup as BS


#API Key import and inicialization        
map_client = googlemaps.Client(API_KEY)


#Code-start, Adress search, Inputs
addressinp = (input("Digite o nome da Rua: "), input("Digite o bairro: "), input("Digite o municipio: "), input("Digite a distancia em km: "))
print('Buscando:')
for i in escopes:
    print(i)
print('Num raio de {}km do endereço: {}'.format(addressinp[3], addressinp[:3]))


#Def kms to meters
def kms_to_meters(kms):
    try:
        return kms * 1_000
    except:
        return 0


#Sentence slice for output
geocode = map_client.geocode(address=addressinp)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))


#%%
#Variables
link_list = []
link_index = 0
link_counter = 0
index = 0
token_counter = 0
distance = kms_to_meters(int(addressinp[3]))
size = len(escopes)
trigger = True
dct = {}
dctaddress = {}

#Scope Search
for i in range(size):
    dct['business_list_%s' % i] = []
    dctaddress['business_list_%s' % i] = []

while trigger == True:
    if index < size:
        search_string = escopes[index]
        print('Searching {} on index {}...'.format(escopes[index], token_counter))
        response = map_client.places_nearby(
            location=(lat, lng),
            keyword=search_string,
            radius=distance
        )
        dct['business_list_%s' % index].extend(response.get('results'))
        next_page_token = response.get('next_page_token')
        time.sleep(2)
    while next_page_token:
        token_counter = token_counter + 1
        response = map_client.places_nearby(
            location=(lat, lng),
            keyword=search_string,
            radius=distance,
            page_token=next_page_token
        )
        dct['business_list_%s' % index].extend(response.get('results'))
        next_page_token = response.get('next_page_token')
        time.sleep(2)
        print('Searching {} on index {}...'.format(escopes[index], token_counter))
    if next_page_token == None:
        print('No more token for {}, going to next escope'.format(escopes[index]))
        token_counter = 0
        if index < size:
            index = index + 1
        if index >= size:
            trigger = False
    else:
        continue


#%%
#DATA STRUCTURE
list_index = 0
while list_index < len(dct):
    for i in dct:
        dctaddress['business_list_%s' % list_index] = pd.DataFrame(dct[i])
        list_index = list_index + 1


#%%
#AUT LINK   PLACE ID
link_index = 0
list_index = 0
size = len(dctaddress) - 1


while link_index < size:
    for i in dctaddress:
        for n in dctaddress[i]:
            if n == 'place_id':
                if list_index < len(dctaddress['business_list_%s' % list_index]):
                    link_list.append('https://www.google.com/maps/place/?q=place_id:' + dctaddress['business_list_%s' % link_index]['place_id'][list_index])
                    print('Appending link {} from list {} ....'.format(list_index, link_index))
                    list_index = list_index + 1
                    if list_index >= len(dctaddress['business_list_%s' % list_index]) - 1:
                            link_index = link_index + 1
                            list_index = 0
#%%
link_index = 0
list_index = 0
size = len(dctaddress) - 1
len(dctaddress['business_list_%s' % link_index]['place_id'][list_index])



#%%
#DROP
for i in drop_dict:
    if i in dctaddress['business_list_%s' % index]:
        dctaddress['business_list_%s' % index].drop(i, axis= 1, inplace= True)


time.sleep(2)
################################################# END CODE 1 ##############################################################

# %%
