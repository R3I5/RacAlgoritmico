# Faça um programa que leia um número indeterminado de valores, correspondente a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1(que não deve ser armazenado)
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem

lista = []
listaInversa = []
qtd = 0
acimaMedia = 0
abaixoDeSete = 0

while True:
    entrada = int(input('Insira uma nota (ou -1 para encerrar): '))
    if entrada == -1:
        break  # encerra o loop se o usuário digitar -1
    lista.append(entrada)  
    qtd = qtd+1
    
listaInversa = list(reversed(lista))
soma = sum(lista)
media = soma/qtd

for nota in lista:
    if nota > media:
        acimaMedia += 1
    if nota < 7:
        abaixoDeSete += 1

print(f'Foram lidas {qtd} notas')
print(f'As notas recebidas foram: {lista}')
print(f'As notas na ordem inversa são: {listaInversa}')
print(f'A soma das notas é: {soma}')
print(f'A média das notas é {media}')
print(f'{acimaMedia} tiveram notas acima da média')
print(f'{abaixoDeSete} tiveram notas abaixo de 7')
print('Obrigado por utilizar o programa!')