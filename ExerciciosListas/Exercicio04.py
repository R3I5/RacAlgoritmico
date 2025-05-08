# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
qtdConsoantes = 0

for i in range(10):
    caracteres = input(f'Digite o {i+1}° caracter: ')
    letras.append(caracteres)
    if caracteres not in vogais:
        consoantes.append(caracteres)
        qtdConsoantes = qtdConsoantes + 1
print(f'As letras são: {letras}')
print(f'Foram digitadas {qtdConsoantes} consoantes')
print(f'As consoantes digitadas são: {consoantes}')