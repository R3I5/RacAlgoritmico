#Escreva uma instrução que represnte a fórmula de bhaskara

import math

a = float(input("Insira o valor de A:"))
b = float(input("Insira o valor de B:"))
c = float(input("Insira o valor de C:"))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("A equação não possui raizes")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(f"O valor do x1 é:{x1}")
    print(f"O valor do x2 é:{x2}")
