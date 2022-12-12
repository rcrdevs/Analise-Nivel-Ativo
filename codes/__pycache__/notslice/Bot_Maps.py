#%%
##########################################################CODE 1 - MAPS REQUEST############################################
#Imports
import geopy
from distutils.log import info
from pickletools import long1
import string
import time
from tokenize import cookie_re
from tracemalloc import stop
from types import coroutine
import googlemaps # pip install googlemaps
import pandas as pd # pip install pandas
import requests
import bs4
from bs4 import BeautifulSoup as BS
import re

#Def miles to meters
def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0

#API Key import and inicialization        
API_KEY = 'AIzaSyDYDmvj32u6j6RF4sPv0WCBWMf5XH7iJHI'
map_client = googlemaps.Client(API_KEY)

#Code-start, Adress search
address = (input("Digite o endereço de referencia: "))
geocode = map_client.geocode(address=address)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

#Escope 1 = Shopping
escope = ('Casas Bahia')
search_string = escope
distance = miles_to_meters(999)
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
shopping_list= (business_list)

#Slice Lat and Lng - Shopping
latshoppinglist = []
lngshoppinglist = []
respshopping = shopping_list
listsize = len(shopping_list)

for i in range(len(respshopping)):
    while i < listsize:
        latshopping = (respshopping[i]['geometry']['location'].get ('lat'))
        lngshopping = (respshopping[i]['geometry']['location'].get ('lng'))
        i = i + 1
        latshoppinglist.append(latshopping)
        lngshoppinglist.append(lngshopping)


lat1 = (latshoppinglist[0:listsize])
lng1 = (lngshoppinglist[0:listsize])

#Dataframe save structure - Shopping
df = pd.DataFrame(shopping_list)
df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
df['latitude'] = lat1
df['longitude'] = lng1

#Escope 2 = Mercado
escope = ('Americanas')
search_string = escope
distance = miles_to_meters(999)
business_list = []


response2 = map_client.places_nearby(
    location=(lat, lng),
    keyword=search_string,
    radius=distance
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
mercado_list= (business_list)

#Slice Lat and Lng - Mercado
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

#Dataframe 2 save
df2 = pd.DataFrame(mercado_list)
df2['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df2['place_id']
df2['latitude'] = lat2
df2['longitude'] = lng2

#Escope 3 = Metrô
escope = ('Magazine Luiza')
search_string = escope
distance = miles_to_meters(999)
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
metro_list= (business_list)

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

#Dataframe 3 save
df3 = pd.DataFrame(metro_list)
df3['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df3['place_id']
df3['latitude'] = lat3
df3['longitude'] = lng3



#Strings das infos do endereço de referencia
geo2 = geopy.geocoders.Nominatim(user_agent="Intro Geocode").reverse(str(lat) + ", " + str(lng))

str(geo2).split(',')

stringsp = (str(geo2[0]).split(','))

rua = (str(stringsp[0]))
região = (stringsp[1])
bairro = (stringsp[2])
Uf = (str(stringsp[3]).split(' '))
#Uf1 = list(Uf[1])
#Uf2 = list(Uf[2])
#Uff = Uf1[0] + Uf2[0]
Pais = stringsp[8]
cidade = stringsp[3]
zoneamento = stringsp[5]
tipologia = stringsp[6]
cep = stringsp[9]
dfgeo = pd.DataFrame(geocode)
link = 'https://www.google.com/maps/place/?q=place_id:' + dfgeo['place_id']
link = link[0]
infos = stringsp[8]

#Dataframe do endereço de referencia
df4 = pd.DataFrame(columns= ['Rua', 'Região', 'Bairro', 'UF', 'Pais', 'Cidade', 'Zoneamento', 'Tipologia', 'CEP', 'Latitude', 'Longitude', 'Link Maps', 'Mais Informações'])
df4 = df4.append({'Rua': rua, 'Região': região, 'Bairro':bairro, 'UF':Uf, 'Pais': Pais, 'Cidade':cidade, 'Zoneamento':zoneamento, 'Tipologia':tipologia, 'CEP':cep, 'Latitude':lat, 'Longitude':lng, 'Link Maps':link, 'Mais Informações':infos }, ignore_index=True)

#Append Dataframes into xlsx sheets
name = input('Digite o nome do arquivo :')
with pd.ExcelWriter (name + '.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    df.to_excel(writer, sheet_name='Shopping', index = False)
    df2.to_excel(writer, sheet_name='Mercado', index = False)
    df3.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False) 
time.sleep(5)
################################################# END CODE 1 ##############################################################

##################################### CODE 2 - DISTANCE AND TIME CALCULATOR ################################################
# Requires API key
#%%
gmaps = googlemaps.Client(key='AIzaSyDYDmvj32u6j6RF4sPv0WCBWMf5XH7iJHI')

# Sources
source = (address)
destShopping = pd.read_excel(name + '.xlsx', sheet_name='Shopping')
destMercado = pd.read_excel(name + '.xlsx', sheet_name='Mercado')
destInfra = pd.read_excel(name + '.xlsx', sheet_name='Infraestrutura de mobilidade')
addr1 = destShopping['vicinity']
addr2 = destMercado['vicinity']
addr3 = destInfra['vicinity']

# Requires cities name

#For Shopping
actual_distance_Shopping = []
time_Shopping = []

for i in addr1:   
    destination = i
    origin = source
    my_dist = gmaps.distance_matrix(origin, destination, mode= 'driving') ["rows"][0]["elements"][0]["distance"]["text"]
    my_dist_time = gmaps.distance_matrix(origin, destination, mode= 'driving') ["rows"][0]["elements"][0]["duration"]["text"]
    actual_distance_Shopping.append(my_dist)
    time_Shopping.append(my_dist_time)

#For Mercado
actual_distance_Mercado = []
time_Mercado = []

for i in addr2:
    destination = i
    origin = source
    my_dist = gmaps.distance_matrix(origin, destination, mode= 'driving') ["rows"][0]["elements"][0]["distance"]["text"]
    my_dist_time = gmaps.distance_matrix(origin, destination, mode= 'driving') ["rows"][0]["elements"][0]["duration"]["text"]
    actual_distance_Mercado.append(my_dist)
    time_Mercado.append(my_dist_time)

#For Metro
actual_distance_Metro = []
time_Metro = []

for i in addr2:
    destination = i
    origin = source
    my_dist = gmaps.distance_matrix(origin, destination, mode= 'driving') ["rows"][0]["elements"][0]["distance"]["text"]
    my_dist_time = gmaps.distance_matrix(origin, destination, mode= 'driving') ["rows"][0]["elements"][0]["duration"]["text"]
    actual_distance_Metro.append(my_dist)
    time_Metro.append(my_dist_time)

# DF Shopping
dfShopping = pd.DataFrame(destShopping)
dfShopping ['Distance'] = actual_distance_Shopping
dfShopping ['Time'] = time_Shopping

# DF Mercado
dfMercado = pd.DataFrame(destMercado)
dfMercado ['Distance'] = actual_distance_Mercado
dfMercado ['Time'] = time_Mercado


# DF Metro
dfMetro = pd.DataFrame(destInfra)
dfMetro['Distance'] = actual_distance_Metro
dfMetro ['Time'] = time_Metro
#fill index with 0

# To Excel
with pd.ExcelWriter (name + '.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    dfShopping.to_excel(writer, sheet_name='Shopping', index = False)
    dfMercado.to_excel(writer, sheet_name='Mercado', index = False)
    dfMetro.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False)


################################################ END CODE 2 ##############################################################

################################################# CODE 3 - DATA CLEANING #################################################
#%%

dataShopping = pd.read_excel(name + '.xlsx', sheet_name='Shopping')
dataMercado = pd.read_excel (name + '.xlsx', sheet_name='Mercado')
dataInfra = pd.read_excel (name + '.xlsx', sheet_name='Infraestrutura de mobilidade')
routeShopping = pd.read_excel(name + '.xlsx', sheet_name='Shopping')
routeMercado = pd.read_excel (name + '.xlsx', sheet_name='Mercado')
routeInfra = pd.read_excel (name + '.xlsx', sheet_name='Infraestrutura de mobilidade')

#Shopping Data Frames
dfShopping = pd.DataFrame(dataShopping)
dfShopping2 = pd.DataFrame(routeShopping)['Distance']
dfShopping3 = pd.DataFrame(routeShopping)['Time']
dfShopping['Distance'] = dfShopping2
dfShopping['Time'] = dfShopping3
    
#Mercado Data Frames
dfMercado = pd.DataFrame(dataMercado)
dfMercado2 = pd.DataFrame(routeMercado)['Distance']
dfMercado3 = pd.DataFrame(routeMercado)['Time']
dfMercado['Distance'] = dfMercado2
dfMercado['Time'] = dfMercado3

#Infra Data Frames
dfInfra = pd.DataFrame(dataInfra)
dfInfra2 = pd.DataFrame(routeInfra)['Distance']
dfInfra3 = pd.DataFrame(routeInfra)['Time']
dfInfra['Distance'] = dfInfra2
dfInfra['Time'] = dfInfra3


#%%
#Drops
dfShopping.drop(['geometry', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)
dfMercado.drop(['geometry', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)
dfInfra.drop(['geometry', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)

#Save
with pd.ExcelWriter (name + '.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    dfShopping.to_excel(writer, sheet_name='Shoppings', index = False)
    dfMercado.to_excel(writer, sheet_name='Mercados', index = False)
    dfInfra.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False)
#################################################### END CODE 3 ############################################################

######################################### CODE 4 - DEMOGRAPHIC DATA ######################################################
#%%
#Imports
import tqdm
import requests
import pandas as pd #Data handling 
import matplotlib.pyplot as plt
import numpy as np #Array handling
import json
import seaborn as sns

url = 'https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/615|616?localidades=N2[all]'#url da Query Builder do IBGE

Data_IBGE = requests.get(url).json()
## Data_IBGE
titulo = Data_IBGE[0]['variavel']
# # titulo
unidVar0 = Data_IBGE[0]['unidade']
unidVar1 = Data_IBGE[1]['unidade']
unidVar0
RR = 4 #Qual região
Area_total = Data_IBGE[0]['resultados'][0]['series'][RR]['serie']['2010']
# # Area_total
Regiao = Data_IBGE[0]['resultados'][0]['series'][RR]['localidade']['nome']
inforeg = ('A região', Regiao, 'tem',  Area_total, unidVar0)


# Preparar dados para representar em um gráfico
dados = []
for i in range(len(Data_IBGE[0]['resultados'][0]['series'])):#cria uma matriz com vetor de dados     
    dados.append( Data_IBGE[0]['resultados'][0]['series'][i]['localidade']['nome'] )#Qual a região
    dados.append( Data_IBGE[0]['resultados'][0]['series'][i]['serie']['2010'] )#"Área total das unidades territoriais"
    dados.append( Data_IBGE[1]['resultados'][0]['series'][i]['serie']['2010'] )#"Habitante por quilômetro quadrado"

matriz_np = np.array(dados)
# # matriz_np
matriz_ajustada = np.reshape(matriz_np, (5, 3))
# # matriz_ajustada
# ## -- Acrescentar nomes para colunas e armazenar tudo em um DataFrame
varName0 = Data_IBGE[0]['resultados'][0]['series'][i]['localidade']['nivel']['nome'] 
varName1 = Data_IBGE[0]['variavel']
varName2 = Data_IBGE[1]['variavel']
colunas = [varName0, varName1, varName2]
df = pd.DataFrame(matriz_ajustada, columns = colunas)
display(df)
# # df


# # Dois gráficos setoriais
labels = np.array(df[varName0])
Var1 = np.array(df[varName1], dtype=float)
Var2 = np.array(df[varName2], dtype=float)

explode1 = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Norte')
explode2 = (0, 0, 0.1, 0, 0)

CC= ['C0', 'C1', 'C2', 'C3', 'C4']#Colors

fig1, ax1 = plt.subplots(1, 2, figsize=(7, 7))
# ## --- Gráfico 1
ax1[0].pie(Var1, explode=explode1, labels=labels, colors= CC, autopct='%1.1f%%',
         shadow=True, startangle=90)
ax1[0].set_title(varName1)
ax1[0].set_position([0, 0.5, 0.5, 0.6])#[left, bottom, width, height

# ## --- Gráfico 2
ax1[1].pie(Var2, explode=explode2, labels=labels, colors= CC, autopct='%1.1f%%',
         shadow=True, startangle=90)
ax1[1].set_title(varName2)
ax1[1].set_position([0.7, 0.5, 0.5, 0.6])
chart1 = plt.gcf()
plt.show()



urlPop = 'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2001|2002|2003|2004|2005|2006|2008|2009|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021/variaveis/9324?localidades=N3[35]'

Data_IBGE_P = requests.get(urlPop).json()
# # Data_IBGE_P
titulo = Data_IBGE_P[0]['variavel']
# # titulo
unid = Data_IBGE_P[0]['unidade']
unid
Ano2 = 2021 #Qual região
Ano1 = 2016 

#Organização JSON
Pop_ano = Data_IBGE_P[0]['resultados'][0]['series'][0]['serie'][str(Ano1)]
Pop_ano2 = Data_IBGE_P[0]['resultados'][0]['series'][0]['serie'][str(Ano2)]
Aumentopop = int(Pop_ano2) - int(Pop_ano)
Localidade = Data_IBGE_P[0]['resultados'][0]['series'][0]['localidade']['nome']

#Organização strings
info1 = ('A', titulo, 'em', Localidade, 'em', Ano1, 'era de',  Pop_ano, unid)
info2 = ('A', titulo, 'em', Localidade, 'em', Ano2, 'era de',  Pop_ano2, unid)
info3 = ('Houve um aumento populacional estimado de:', Aumentopop,'pessoas em', Localidade, 'entre os periodos de: ', Ano1, 'e', Ano2,'.','(',Ano2 - Ano1, 'Anos)')

#%%
sentence1 = ""
sentence2 = ""
sentence3 = ""
sentence4 = ""

for word1 in info1:
    sentence1 += str(word1) + " "
for word2 in info2:
    sentence2 += str(word2) + " "
for word3 in info3:
    sentence3 += str(word3) + " "
for word4 in inforeg:
    sentence4 += str(word4) + " " 

df4['Estimativa Populacional Anterior'] = sentence1
df4['Estimativa Populacional Atual'] = sentence2
df4['Auimento Populacional Estimado'] = sentence3
df4['Area Total'] = sentence4

#%%
#Save
with pd.ExcelWriter (name + '.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    dfShopping.to_excel(writer, sheet_name='Shopping', index = False)
    dfMercado.to_excel(writer, sheet_name='Mercado', index = False)
    dfInfra.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False)
############################################### END CODE 4 #############################################################


########################################## CODE 5 - ETARY DATA #########################################################
#%%
url = 'https://servicodados.ibge.gov.br/api/v3/agregados/2149/periodos/2000/variaveis/289?localidades=N3[35]&classificacao=303[6853]|2[4,5]|58[all]'
#url = 'https://servicodados.ibge.gov.br/api/v3/agregados/2149/periodos/2000/variaveis/289?localidades=N3[41]&classificacao=303[6854]|2[4,5]|58[all]'

Data_IBGE = requests.get(url).json()
Data_IBGE

# # Data_IBGE
titulo = Data_IBGE[0]['variavel']
titulo
unidVar0 = Data_IBGE[0]['unidade']
# # unidVar1 = Data_IBGE[1]['unidade']
unidVar0
RR = 2
Var1 = Data_IBGE[0]['resultados'][RR]['classificacoes'][1]['categoria']['4']#Sexo
Var2 = Data_IBGE[0]['resultados'][RR]['classificacoes'][2]['categoria']['1141']#Faixa etária
Var3 = Data_IBGE[0]['resultados'][RR]['series'][0]['serie']['2000']#Valor
Var1, Var2, Var3 
# #Regiao = Data_IBGE[0]['resultados'][0]['series'][RR]['localidade']['nome']

# # Preparar dados para representar em um gráfico
dados = []
n1 = np.array((range(1140, 1156, 1)))
n2 = [2503]
vv = [*n1, *n2]

PP = 34
for i in range( PP ):#cria uma matriz com vetor de dados
   if i<17: 
     S = '4'
     L = i
     C = 1
   else:
     S = '5'
     L = i-17
     i = i + 1 
     C = -1  
   dados.append( Data_IBGE[0]['resultados'][i+1]['classificacoes'][1]['categoria'][S] )#Sexo
   dados.append( Data_IBGE[0]['resultados'][i+1]['classificacoes'][2]['categoria'][str(vv[L])] )#Faixa etária
   dados.append( pd.to_numeric(Data_IBGE[0]['resultados'][i+1]['series'][0]['serie']['2000'])*C )#Valor

matriz_np = np.array(dados)
# # matriz_np
matriz_ajustada = np.reshape(matriz_np, (PP, 3))
# # matriz_ajustada
# ## -- Acrescentar nomes para colunas e armazenar tudo em um DataFrame
varName0 = Data_IBGE[0]['resultados'][RR]['classificacoes'][1]['nome']#Sexo
varName1 = Data_IBGE[0]['resultados'][1]['classificacoes'][2]['nome']#Faixa etaria
varName2 = Data_IBGE[0]['variavel']
colunas = [varName0, varName1, varName2]

colunas = [varName0, 'Faixa_Etaria', 'Brasileiros_natos']
df = pd.DataFrame(matriz_ajustada, columns = colunas)
#df

# Draw Plot
plt.figure(figsize=(10,8), dpi= 80)

group_col = varName0
order_of_bars = df.Faixa_Etaria.unique()[::-1]

colunas = [varName0, 'Faixa_Etaria', 'Brasileiros_natos']
df[colunas[2]] = pd.to_numeric(df[colunas[2]])

colors = [plt.cm.Spectral(i/float(len(df[group_col].unique())-1)) for i in range(len(df[group_col].unique()))]

for c, group in zip(colors, df[group_col].unique()):
     sns.barplot(x=colunas[2], y= colunas[1], data=df.loc[df[group_col]==group, :], order=order_of_bars, color=c, label=group)

# # Decorations
plt.xlabel(colunas[2])
plt.ylabel(colunas[1])
plt.yticks(fontsize=12)
plt.title("Brasileiros natos em São Paulo por sexo e grupos de idade", fontsize=22)
plt.legend()
chart2 = plt.gcf() 
plt.show()

#CALCULO DA MÉDIA ETARIA PONDERADA
df['Brasileiros_natos'] = df['Brasileiros_natos'].abs()
dfh = pd.DataFrame(df['Brasileiros_natos'][:17])
dfm = pd.DataFrame(df['Brasileiros_natos'][17:])

idades = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82]
pesosh = list(dfh.values)
pesosm = list(dfm.values)

idades_pesosh = zip(idades, pesosh)
idades_pesosm = zip(idades, pesosm)

soma_idades_pesosh = 0
soma_idades_pesom = 0

for idade, peso in idades_pesosh:
  soma_idades_pesosh += idade * peso

for idade, peso in idades_pesosm:
  soma_idades_pesom += idade * peso

soma_pesosh = 0
soma_pesosm = 0

for peso in pesosh:
  soma_pesosh += peso

for peso in pesosm:
  soma_pesosm += peso


media_etaria_ponderadah = (soma_idades_pesosh / soma_pesosh)
media_etaria_ponderadam = (soma_idades_pesom / soma_pesosm)

info1 = ('A média etaria de homens nessa região é de:', media_etaria_ponderadah, 'anos')
info2 = ('A média etaria de mulheres nessa região é de:', media_etaria_ponderadam, 'anos')

sentence1 = ""
sentence2 = ""

for word1 in info1:
    sentence1 += str(word1) + " "
for word2 in info2:
    sentence2 += str(word2) + " "

df4['Média Etária Homens'] = sentence1
df4['Média Etária Mulheres'] = sentence2

#Save
with pd.ExcelWriter (name + '.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    dfShopping.to_excel(writer, sheet_name='Shopping', index = False)
    dfMercado.to_excel(writer, sheet_name='Mercado', index = False)
    dfInfra.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False)
################################################## END CODE 5 #########################################################


########################################## CODE 6 - PIB DATA ###########################################################
#%%
url = 'https://apisidra.ibge.gov.br/values/t/5938/n9/31030,33018,35061,41037/v/37,513,517,525,6575/p/last%201/d/v37%200,v513%200,v517%200,v525%200,v6575%200'
#url2 = 'https://apisidra.ibge.gov.br/values/t/5938/n1/all/n2/all/n3/all/n8/3512/n9/35061/n6/3550308/v/37,498,513,517,525,543,6575/p/last%201/d/v37%200,v498%200,v513%200,v517%200,v525%200,v543%200,v6575%200'
data = requests.get(url).json()

#PIB Data Structure
PIB_sp = data[11]['V']
PIB_agropecuario = data[12]['V']
PIB_industrial = data[13]['V']
PIB_administrativo = data[14]['V']
PIB_serviços = data[15]['V']

#Dataframe Structure
df4['PIB da Cidade (Mil Reais)'] = PIB_sp
df4['PIB Agropecuario (Mil Reais)'] = PIB_agropecuario
df4['PIB Industrial (Mil Reais)'] = PIB_industrial
df4['PIB Administrativo (Mil Reais)'] = PIB_administrativo
df4['PIB Serviços (Mil Reais)'] = PIB_serviços

#Save
with pd.ExcelWriter (name + '.xlsx') as writer:
    df4.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    dfShopping.to_excel(writer, sheet_name='Shopping', index = False)
    dfMercado.to_excel(writer, sheet_name='Mercado', index = False)
    dfInfra.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False)
################################################## END CODE 6 #############################################################

################################################## CODE 7 - OUTPUT ORGANIZER ###############################################
# %%
import xlwings as xw
xls = (name + '.xlsx')
wb = xw.Book(xls)
sht = wb.sheets[0]
sht1 = wb.sheets[1]

def insert_heading(rng, text):
    rng.value = text
    rng.font.bold = True
    rng.font.size = 20
    rng.font.color = (0, 0, 139)

insert_heading(sht.range("A4"), "Charts")

sht.pictures.add(
    chart1,
    name = "Matplotlib",
    update = True,
    left = sht.range("C4").left,
    top = sht.range("C4").top,
    height=200,
    width=400,
)
sht.pictures.add(
    chart2,
    name = "Matplotlib2",
    update = True,
    left = sht.range("L4").left,
    top = sht.range("L4").top,
    height=200,
    width=300,
)
#%%
insert_heading(sht.range("S4"), "Ancoras imobiliarias")

################################################## END CODE 7 #############################################################