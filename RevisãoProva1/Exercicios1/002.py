# 2. Escreva uma instrução em python que calcule o perímetro de um círculo

import math

raio = float(input('Digite o raio do círculo: '))
pi = math.pi
c = 2 * pi * raio
print(f'O perimetro é: {c:.2f}')