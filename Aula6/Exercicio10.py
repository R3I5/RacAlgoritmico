"""
Escreva um programa que solicite ao usuario um numero e imprima se ele é par ou impar, utilizando um laço de repetição while
"""

numero = int(input("Digite um número: "))

while True:
    if numero % 2 == 0:
        print("Número Par")
    else:
        print("Número Ímpar")
    break
