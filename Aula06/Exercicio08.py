"""
Escreva um programa que calcule a média de 5 números inseridos pelo usuario, utilizando um laço de repetição while
"""

x = 0
soma = 0
while(x<5):
    x = x + 1
    valor = float(input('Digite 5 números: '))
    soma += valor
    
media = soma / 5
print(media)