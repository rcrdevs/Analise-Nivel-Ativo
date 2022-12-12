#%%
#Imports
from re import I
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from ApiRequests import addressinp3
from IBGEDatabase import dictreg, dictregnum, dictibge
import time

################# Automatização de plotagem da area da região
url = 'https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/615|616?localidades=N2[all]'#url da Query Builder do IBGE

#Data get
Data_IBGE = requests.get(url).json()
titulo = Data_IBGE[0]['variavel']


time.sleep(3)
#For dictionaries
for i in dictreg:
    if addressinp3 == i:
        value = dictreg.get(i)
        
time.sleep(3)
for i in dictregnum:
    if value == i:
        value = dictregnum.get(i)

#Organização JSON variaveis
unidVar0 = Data_IBGE[0]['unidade']
unidVar1 = Data_IBGE[1]['unidade']
unidVar0
RR = int(value)

#Organização outputs
Area_total = Data_IBGE[0]['resultados'][0]['series'][RR]['serie']['2010']
Regiao = Data_IBGE[0]['resultados'][0]['series'][RR]['localidade']['nome']
inforeg = ('A região', Regiao, 'tem',  Area_total, unidVar0)

### Preparar dados para representar em um gráfico
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
dfs = pd.DataFrame(matriz_ajustada, columns = colunas)
# # df


# # Dois gráficos setoriais
labels = np.array(dfs[varName0])
Var1 = np.array(dfs[varName1], dtype=float)
Var2 = np.array(dfs[varName2], dtype=float)

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
##############################CHART PLOTS

#### DATA BASE LOCALIZATIONS
for i in dictibge:
    if addressinp3 == i:
        location = dictibge.get(i)

#Data get
urlPop = 'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2001|2002|2003|2004|2005|2006|2008|2009|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021/variaveis/9324?localidades=N3' + location
Data_IBGE_P = requests.get(urlPop).json()
titulo = Data_IBGE_P[0]['variavel']
unid = Data_IBGE_P[0]['unidade']
unid
Ano2 = 2021 
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

#SENTENCES ORGANIZATION
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
# %%

