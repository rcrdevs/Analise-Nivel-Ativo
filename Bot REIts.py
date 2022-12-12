#%%
from urllib import request
from wsgiref import headers
from pandas_datareader import data as web
from openpyxl import Workbook, load_workbook
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter as ws
from datetime import date
from datetime import datetime

######REIT's
#%%
#DATA GET
data = int(input('Pegar a cotação historica de quantos anos?'))
date_time = date.today()
date_later = date_time.year - data
date_later = date_time.day, "-", '0', date_time.month, "-", date_later
datesentence = ""

for word in date_later:
    datesentence += str(word)

name = input('Digite o ticker do REIT')
cotacao = web.DataReader(name, data_source = 'yahoo', start = datesentence)
cotacao = cotacao['Adj Close']

#%%
#DATABASE WAY
sheetbase = r"G:\.shortcut-targets-by-id\1NOci7ltXs7AZpOZWLSpFiM0AB_6dE91G\NewPort\11. Outros\Projeto - Panorama de Mercado\Histórico - REITs.xlsx"

#%%
#DATA SAVE
outWorkbook = ws.Workbook(sheetbase)
outSheet = outWorkbook.add_worksheet(name + " " + "Dados")
index = 0
factor = 2
outSheet.write("A1", name)
emptylst = []
emptylst.append(cotacao)
emptylstindex = []
emptylstindex.append(cotacao.index)


while index < len(cotacao):
    for i in emptylst:
        dt = i.index[index]
        dt = datetime.timestamp(dt)
        dt = datetime.fromtimestamp(dt).strftime('%d-%m-%y')
        outSheet.write("A" + str(factor), dt)
        factor = factor + 1
        index = index + 1


index = 0
factor = 2
for row in cotacao:
    outSheet.write("B" + str(factor), cotacao[index])
    factor = factor + 1
    index = index + 1

outWorkbook.close()
#########################################