# Criar um programa que efetua a soma de duas matrizes 3x3, sabendo que a soma das matrizes 3x3
# é uma nova matriz 3x3 onde cada elemento é resultado da soma dos elementos das matrizes na mesma posição

matriz1 = []
matriz2 = []
matriz3 = []

for i in range(3):
    aj1m1 = int(input(f'Insira um valor de a{i+1}1 da primeira matriz: '))
    aj2m1 = int(input(f'Insira um valor de a{i+1}2 da primeira matriz: '))
    aj3m1 = int(input(f'Insira um valor de a{i+1}3 da primeira matriz: '))
    matriz1.append([aj1m1, aj2m1, aj3m1])
print('Matriz 1:')
print(matriz1)

for i in range(3):
    aj1m2 = int(input(f'Insira um valor de a{i+1}1 da segunda matriz: '))
    aj2m2 = int(input(f'Insira um valor de a{i+1}2 da segunda matriz: '))
    aj3m2 = int(input(f'Insira um valor de a{i+1}3 da segunda matriz: '))
    matriz2.append([aj1m2, aj2m2, aj3m2])
print('Matriz 2:')
print(matriz2)

for i in range(3):
    for j in range(3):
        soma = matriz1[i][j] + matriz2[i][j] #percorre cada linha e coluna somando os valores respectivos a cada posição
        matriz3.append(soma)
print('A soma das matrizes 1 e 2 é: ')
print(matriz3)
