# Faça um programa que leia 20 números inteiros e armazene-os num vetor
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
impares = []
for i in range(10):
    num = int(input('Insira 1 número inteiro: '))
    numeros.append(num)
    if num %2 ==0:
        pares.append(num)
    else:
        impares.append(num)
    
print(f'Os números inseridos foram : {numeros}')
print(f'Os números pares inseridos foram: {pares}')
print(f'Os números impares inseridos foram: {impares}')