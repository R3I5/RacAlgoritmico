# 4. Funções Modulares (Exemplo: Área do Cilindro)
# Dividir um problema em funções menores torna o código mais legível e fácil de manter.

# Python

import math # Para usar math.pi

def calcular_area_base_circulo(raio):
    """Calcula a área de um círculo (base do cilindro)."""
    return math.pi * (raio ** 2)

def calcular_area_lateral_cilindro(raio, altura):
    """Calcula a área lateral de um cilindro."""
    return 2 * math.pi * raio * altura

def calcular_area_total_cilindro(raio, altura):
    """Calcula a área total de um cilindro chamando outras funções."""
    area_base = calcular_area_base_circulo(raio)
    area_lateral = calcular_area_lateral_cilindro(raio, altura)
    
    # Área total = 2 * área da base + área lateral
    area_total = (2 * area_base) + area_lateral
    return area_total

# Exemplo de uso:
raio_cilindro = 3
altura_cilindro = 5
area_do_cilindro = calcular_area_total_cilindro(raio_cilindro, altura_cilindro)

print(f"Raio: {raio_cilindro}, Altura: {altura_cilindro}")
# Exemplo de como as funções internas seriam chamadas:
# print(f"Área da base: {calcular_area_base_circulo(raio_cilindro)}")
# print(f"Área lateral: {calcular_area_lateral_cilindro(raio_cilindro, altura_cilindro)}")
print(f"Área total do cilindro: {area_do_cilindro:.2f}") # :.2f para formatar com 2 casas decimais
# Saída esperada (aproximada): Área total do cilindro: 150.80