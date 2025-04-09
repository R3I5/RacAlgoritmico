"""
Escreva um programa que imprima os numeros primos de 1 a 100 utilizando um laço de repetição for e range
"""
# Lista para armazenar os números primos
primos = []

# Loop de 2 a 100
for num in range(2, 101):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

# Imprime a lista de números primos
print("Números primos de 1 a 100:")
print(primos)
