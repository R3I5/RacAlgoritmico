# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros valores

listaA = []
listaB = []

for i in range(10):
    nums1 = int(input(f'Digite o {i+1}°  numero do primeiro vetor: '))
    listaA.append(nums1)
for a in range(10):
    nums2 = int(input(f'Digite o {a+1}°  numero do segundo vetor: '))
    listaB.append(nums2)

print(f'Os numeros da primeira lista são: {listaA}')
print(f'Os numeros da segunda lista são: {listaB}')

listaC = []
for b in range(10): 
    listaC.append(listaA[b])
    listaC.append(listaB[b])

print(f'Os numeros intercalados são: {listaC}')