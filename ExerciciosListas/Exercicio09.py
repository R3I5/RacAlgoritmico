# Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor

vetorA = []
vetorB = []
for i in range(10):
    valor = int(input(f'Insira o valor {i+1}: '))
    valorQuadrado = valor ** 2
    vetorA.append(valor)
    vetorB.append(valorQuadrado)
    soma = sum(vetorB)
print(f'Os valores do vetor A são: {vetorA}')
print(f'O quadrado dos valores do vetor A são: {vetorB}')
print(f'A soma dos quadrados é {soma}')

