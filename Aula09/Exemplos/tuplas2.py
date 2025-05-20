# Exemplo 2:
# Elaborar um programa que cria uma tupla contendo duas listas como dados.
# Alterar os dados da primeira lista e verificar se ocorre mudançca de dados da tupla

tuplaComLista = ([1,2,3], [4,5,6])
print(id(tuplaComLista[0]))
tuplaComLista[0].append(9)
print(tuplaComLista)
print(id(tuplaComLista[0]))