#%%
import ApiRequests
from Distance_Time import *
from DadosDemograficos import *
from DadosEtarios import *
from PIB import *

##############COMPLETAR DICIONARIO IBGE################
#%%
##DFS RENAME
df.rename(columns={'name': 'Name', 'opening_hours': 'Open or Closed now', 'rating': 'Google Rating', 'types': 'Types', 'user_ratings_total': 'Ratings Total', 'vicinity': 'Vicinity'}, inplace = True)
df2.rename(columns={'name': 'Name', 'opening_hours': 'Open or Closed now', 'rating': 'Google Rating', 'types': 'Types', 'user_ratings_total': 'Ratings Total', 'vicinity': 'Vicinity'}, inplace = True)
df3.rename(columns={'name': 'Name', 'opening_hours': 'Open or Closed now', 'rating': 'Google Rating', 'types': 'Types', 'user_ratings_total': 'Ratings Total', 'vicinity': 'Vicinity'}, inplace = True)

#%%
##OUPUT DECORATIONS
import xlwings as xw
import pandas as pd
import seaborn as sns

empty = None
fake = pd.DataFrame(empty)

with pd.ExcelWriter (name + '.xlsx') as writer:
    fake.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    df.to_excel(writer, sheet_name=escope1, index = False)
    df2.to_excel(writer, sheet_name=escope2, index = False)
    df3.to_excel(writer, sheet_name=escope3, index = False) 
time.sleep(3)

##XLWINGS
xls = (name + '.xlsx')
wb = xw.Book(xls)
sht = wb.sheets[0]
sht1 = wb.sheets[1]
sht2 = wb.sheets[2]
sht3 = wb.sheets[3]

def insert_heading(rng, text):
    rng.value = text
    rng.font.bold = True
    rng.font.size = 16
    rng.font.color = (0, 0, 139)

def insert_text(rng, text):
    rng.value = text
    rng.font.bold = True
    rng.font.size = 12
    rng.font.color = (0, 0, 0)


insert_heading(sht.range("A10"), "Charts")

sht.pictures.add(
    chart1,
    name = "Matplotlib",
    update = True,
    left = sht.range("B10").left,
    top = sht.range("B10").top,
    height=200,
    width=400,
)
sht.pictures.add(
    chart2,
    name = "Matplotlib2",
    update = True,
    left = sht.range("K10").left,
    top = sht.range("K10").top,
    height=200,
    width=300,
)


## AUTOMATIZAÇÃO DECORATIONS 
insert_heading(sht.range("A1"), 'Informações sobre o endereço de referencia')
insert_heading(sht.range("J1"), 'Ancoras Imobiliarias')

varow = 'A'
varow2 = 'B'
index = 0
size = len(df4list)
sizeloop = (int(size/1.5))

while index < size:
    insert_text(sht.range(varow + str(index + 2)), df4list[index])
    index = index + 1
    if index >= sizeloop:
        break

while index < size:
    insert_text(sht.range(varow2 + str(index + 2 - sizeloop)), df4list[index])
    index = index + 1
    if index >=size:
        break

slice1 = (sht1.range('A1:M3').options(pd.DataFrame).value)
slice2 = (sht2.range('A2:M3').options(pd.DataFrame).value)
slice3 = (sht3.range('A2:M3').options(pd.DataFrame).value)

boldtext = sht.range('J2:V8')
headertext = sht.range('A1:V1')
headertext2 = sht.range('A2:V2')
table1 = sht.range('A2:H8')
breaker = sht.range('I1:I8')
tablefin = sht.range('A9:V9')

sht.range("J2").value = slice1
sht.range("J5").value = slice2
sht.range("J7").value = slice3

boldtext.api.Font.Bold = True
boldtext.api.Font.Size = 12
boldtext.color = (242,240,232)
headertext.color = (222,219,206)
headertext2.api.Font.Size = 13
table1.color = (242,240,232)
breaker.color = (222,219,206)
tablefin.color = (222,219,206)
