# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
vogais = [a, e, i, o, u]
for i in range(10):
    caracteres = input(f'Digite o {i+1} caracter: ')
    vetor.append(caracteres)
print(vetor)