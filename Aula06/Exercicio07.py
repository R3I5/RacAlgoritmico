"""
Escreva um programa que solicite ao usuario um numero e imprima a tabuada deste numero de 1 a 10, utilizando um laço de repetição for
"""

x = int(input('Digite um número:'))
y = 0
for i in range(1,11):
    y = x * i
    print(y)
    