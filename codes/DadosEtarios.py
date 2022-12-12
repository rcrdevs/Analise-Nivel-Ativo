#SCRIPT DADOS DEMOGRAFICOS 2 - Piramide Etaria
#%%
import requests
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import json
import seaborn as sns
from IBGEDatabase import dictibge, dictage
from ApiRequests import addressinp3, df4list, df0

for i in dictibge:
    if addressinp3 == i:
        urlvalue = dictibge.get(i)
for i in dictage:
    if addressinp3 == i:
        urlvalue2 = dictage.get(i)

url = 'https://servicodados.ibge.gov.br/api/v3/agregados/2149/periodos/2000/variaveis/289?localidades=N3' + urlvalue + '&classificacao=303' + urlvalue2 + '|2[4,5]|58[all]'

#%%
#Data Get
Data_IBGE = requests.get(url).json()
titulo = Data_IBGE[0]['variavel']


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

#Matrizes
matriz_np = np.array(dados)
matriz_ajustada = np.reshape(matriz_np, (PP, 3))

### -- Acrescentar nomes para colunas e armazenar tudo em um DataFrame
varName0 = Data_IBGE[0]['resultados'][1]['classificacoes'][1]['nome']#Sexo
varName1 = Data_IBGE[0]['resultados'][1]['classificacoes'][2]['nome']#Faixa etaria
varName2 = Data_IBGE[0]['variavel']
colunas = [varName0, varName1, varName2]
colunas = [varName0, 'Faixa_Etaria', 'Brasileiros_natos']
dff = pd.DataFrame(matriz_ajustada, columns = colunas)

# Draw Plot
plt.figure(figsize=(10,8), dpi= 80)

group_col = varName0
order_of_bars = dff.Faixa_Etaria.unique()[::-1]

colunas = [varName0, 'Faixa_Etaria', 'Brasileiros_natos']
dff[colunas[2]] = pd.to_numeric(dff[colunas[2]])

colors = [plt.cm.Spectral(i/float(len(dff[group_col].unique())-1)) for i in range(len(dff[group_col].unique()))]

for c, group in zip(colors, dff[group_col].unique()):
     sns.barplot(x=colunas[2], y= colunas[1], data=dff.loc[dff[group_col]==group, :], order=order_of_bars, color=c, label=group)

# # Decorations
plt.xlabel(colunas[2])
plt.ylabel(colunas[1])
plt.yticks(fontsize=12)
plt.title("Brasileiros natos nesta região por sexo e grupo de idade", fontsize=22)
plt.legend()
chart2 = plt.gcf() 
plt.show()
#%%


#CALCULO DA MÉDIA ETARIA PONDERADA
dff['Brasileiros_natos'] = dff['Brasileiros_natos'].abs()
dfh = pd.DataFrame(dff['Brasileiros_natos'][:17])
dfm = pd.DataFrame(dff['Brasileiros_natos'][17:])

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
df4list.append(sentence1)
for word2 in info2:
    sentence2 += str(word2) + " "
df4list.append(sentence2)

df0 = pd.DataFrame(columns = df4list)
################################################## END CODE 5 #########################################################
