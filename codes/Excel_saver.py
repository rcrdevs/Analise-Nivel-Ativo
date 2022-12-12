name = input('Digite o nome do arquivo :')
with pd.ExcelWriter (name + '.xlsx') as writer:
    df0.to_excel(writer, sheet_name='Endereço de Referencia', index = False)
    df.to_excel(writer, sheet_name=escope1, index = False)
    df2.to_excel(writer, sheet_name=escope2, index = False)
    df3.to_excel(writer, sheet_name=escope3, index = False) 
time.sleep(2)