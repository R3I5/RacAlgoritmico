# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

numeros = []
multiplicação = 1

for i in range(5):
    num = int(input(f'Insira o {i+1}° número inteiro: '))
    numeros.append(num)
    soma = sum(numeros)
for i in numeros:
    multiplicação *= i
    
print(f'Os números inseridos foram: {numeros}')
print(f'A soma dos valores é: {soma}')
print(f'A multiplicação dos números é: {multiplicação}')