"""
Escreva um programa que calcule o fatorial de um número inserido pelo usuario utilizando um laço de repetição while
"""

x = float(input('Insira um número:'))
y = 1
while(x>0):
    y = y * x
    x = x - 1
    print(y)
    