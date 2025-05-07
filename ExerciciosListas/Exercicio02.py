# Faça um programa que leia um vetor de 10 números reais e mostre os na ordem inversa

vetor = []
for i in range(10):
    numeros = int(input(f'Digite o {i+1}° numero: '))
    vetor.append(numeros)
print(f'Vetor na ordem correta: {vetor}')
vetorInvertido = vetor[::-1]
print(f'O vetor na ordem invertida: {vetorInvertido}')
