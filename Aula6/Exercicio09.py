"""
Escreva um programa que imprima os numeros primos de 1 a 100 utilizando um laço de repetição for e range
"""

for i in range(1,101):
    if i<2:
        continue
    eh_primo = True
    for j in range(2,1):
        if i % j == 0:
            eh_primo = False
        break
    if eh_primo:
        print(i)
