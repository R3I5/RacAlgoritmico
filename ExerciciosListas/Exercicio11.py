# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada

listaA = []
listaB = []
listaC = []

for i in range(10):
    nums1 = int(input(f'Digite o {i+1}°  numero do primeiro vetor: '))
    listaA.append(nums1)
for a in range(10):
    nums2 = int(input(f'Digite o {a+1}°  numero do segundo vetor: '))
    listaB.append(nums2)
for b in range(10):
    nums3 = int(input(f'Digite o {b+1}°  numero do terceiro vetor: '))
    listaC.append(nums3)

print(f'Os numeros da primeira lista são: {listaA}')
print(f'Os numeros da segunda lista são: {listaB}')
print(f'Os numeros da terceira lista são: {listaC}')

listaD = []
for c in range(10): 
    listaD.append(listaA[c])
    listaD.append(listaB[c])
    listaD.append(listaC[c])

print(f'Os numeros intercalados são: {listaD}')