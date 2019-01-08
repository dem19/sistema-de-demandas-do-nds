

data_cad = input('Informe a Data de cadastro: ')
data_ent = input('Informe a Data de entrega: ')

lista_data = data_cad.split('-')
lista_data.reverse()
data_cadastro = '-'.join(lista_data)

lista_data = data_ent.split('-')
lista_data.reverse()
data_entrega = '-'.join(lista_data)

print(data_cadastro)
print(data_entrega)