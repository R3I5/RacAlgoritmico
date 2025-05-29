# 1 - Estruturas de Dados Fundamentais
# 1.a - Listas(lists)
"""
    a. Listas (Lists)
    O que são? Coleções ordenadas e mutáveis de itens. Isso significa que você pode adicionar, remover ou alterar elementos depois que a lista é criada, e a ordem dos elementos é preservada.
    Sintaxe: Definidas por colchetes [], com itens separados por vírgulas.
    Exemplos:
"""
# Criação
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
lista_mista = [10, "texto", True, 3.14]

# Acessando elementos (índice começa em 0)
print(frutas[0])        # Saída: maçã
print(numeros[1:3])     # Saída: [2, 3] (fatiamento)

# Modificando elementos
frutas[1] = "morango"
print(frutas)           # Saída: ['maçã', 'morango', 'laranja']

# Adicionando elementos
frutas.append("uva")    # Adiciona ao final
print(frutas)           # Saída: ['maçã', 'morango', 'laranja', 'uva']
frutas.insert(1, "abacaxi") # Adiciona na posição 1
print(frutas)           # Saída: ['maçã', 'abacaxi', 'morango', 'laranja', 'uva']

# Removendo elementos
frutas.remove("morango")
print(frutas)           # Saída: ['maçã', 'abacaxi', 'laranja', 'uva']
del frutas[0]
print(frutas)           # Saída: ['abacaxi', 'laranja', 'uva']

# Uso comum: Quando você precisar de uma coleção de itens que pode ser 
# alterada(adicionar, remover, modificar) e a ordem dos itens é importante