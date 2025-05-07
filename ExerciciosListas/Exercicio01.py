# Faça um programa que leia um vetor de 5 números inteiros e mostre-os

vetor = []
for i in range(5):
    numeros = int(input(f'Digite o numero {i+1}: '))
    vetor.append(numeros)
print(vetor)