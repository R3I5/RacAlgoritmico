#Criar um programa que solicite ao usuário 2 listas com 5 elementos cada
#Como resultado, criar uma terceira lista que intercala os elementos das duas listas

lista1 = []
lista2 = []

for i in range(5):
    nums1 = int(input(f'Digite o {i+1}° numero da primeira lista: '))
    lista1.append(nums1)
for a in range(5):
    nums2 = int(input(f'Digite o {a+1}° numero da segunda lista: '))
    lista2.append(nums2)
    
print(f'Os numeros da primeira lista são: {lista1}')
print(f'Os numeros da segunda lista são: {lista2}')

lista3 = []
for b in range(5):
    lista3.append(lista1[b])
    lista3.append(lista2[b])
    
print(f'Os numeros da terceira lista são: {lista3}')


