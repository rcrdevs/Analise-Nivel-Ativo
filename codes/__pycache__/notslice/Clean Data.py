import pandas as pd

dataShopping = pd.read_excel('outputs/outputaracaju.xlsx', sheet_name='Shopping')
dataMercado = pd.read_excel ('outputs/outputaracaju.xlsx', sheet_name='Mercado')
dataInfra = pd.read_excel ('outputs/outputaracaju.xlsx', sheet_name='Infraestrutura de mobilidade')
routeShopping = pd.read_excel('outputs/outputaracaju.xlsx', sheet_name='Shopping')
routeMercado = pd.read_excel ('outputs/outputaracaju.xlsx', sheet_name='Mercado')
routeInfra = pd.read_excel ('outputs/outputaracaju.xlsx', sheet_name='Infraestrutura de mobilidade')

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


#Drops
dfShopping.drop(['geometry', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)
dfMercado.drop(['geometry', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)
dfInfra.drop(['geometry', 'icon_background_color', 'icon_mask_base_uri', 'photos', 'place_id', 'plus_code', 'reference', 'scope', 'icon'], axis= 1, inplace= True)

name = input('Digite o nome do arquivo :')
with pd.ExcelWriter (name + '.xlsx') as writer:
    dfShopping.to_excel(writer, sheet_name='Shoppings', index = False)
    dfMercado.to_excel(writer, sheet_name='Mercados', index = False)
    dfInfra.to_excel(writer, sheet_name='Infraestrutura de mobilidade', index = False)

