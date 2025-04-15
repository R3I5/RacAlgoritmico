# 3. Dado um retângulo de lado a = 7 e área = 63, escreva:
# 3.1 Uma instrução em python que calcule o valor do lado B
# 3.2 Uma instrução que calcule a diagonal deste retângulo.

import math

ladoA = 7
area = 63
ladoB = area/ladoA
print(ladoB)
diagonal = math.sqrt((ladoA**2)+(ladoB**2))
print(diagonal)