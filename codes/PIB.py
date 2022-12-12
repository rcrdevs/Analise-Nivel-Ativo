import requests as r
from IBGEDatabase import dictsidra
from ApiRequests import addressinp3
import time

url = 'https://apisidra.ibge.gov.br/values/t/5938/n3/all/v/37,513,517,525,6575/p/2014,2019/d/v37%200,v513%200,v517%200,v525%200,v6575%200'
data = r.get(url).json()

for i in dictsidra:
    if addressinp3 == i:
        value = dictsidra.get(i)

time.sleep(3)

index = 1 + int(value)

#
PIB_geral_2014 = data[index]['V']
PIB_geral_2019 = data[index+1]['V']
PIB_agropecuario_2014 = data[index+2]['V']
PIB_agropecuario_2019 = data[index+3]['V']
PIB_industrial_2014 = data[index+4]['V']
PIB_industrial_2019 = data[index+5]['V']
PIB_admin_2014 = data[index+6]['V']
PIB_admin_2019 = data[index+7]['V']
PIB_serviços_2014 = data[index+8]['V']
PIB_serviços_2019 = data[index+9]['V']
# %%
