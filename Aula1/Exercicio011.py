# Dado um retângulo de lado a=7 e área 63, escreva:
# Uma instrução em Python que calcule o valor do B

import math

ladoA = 7
area = 63
ladoB = area/ladoA
print(f"O valor do lado B é:{ladoB}")
d = math.sqrt((ladoA**2)+(ladoB**2))
print(f"O valor da diagonal é:{d:.2f}")

