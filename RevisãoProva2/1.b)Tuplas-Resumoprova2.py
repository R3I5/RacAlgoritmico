# b. Tuplas (Tuples)
# O que são? Coleções ordenadas e imutáveis de itens. Uma vez criadas, seus elementos não podem ser alterados, adicionados ou removidos.
# Sintaxe: Definidas por parênteses (), com itens separados por vírgulas.
# Exemplos:
# Python

# Criação
coordenadas = (10, 20)
cores_rgb = (255, 0, 128)
meses = ("Janeiro", "Fevereiro", "Março")
tupla_um_item = (1,) # A vírgula é essencial para tupla de um item

# Acessando elementos
print(coordenadas[0])   # Saída: 10
print(meses[1])         # Saída: Fevereiro

# Tentativa de modificação (gera erro!)
# coordenadas[0] = 5  # TypeError: 'tuple' object does not support item assignment
# Uso comum: Para dados que não devem ser alterados após a criação, como coordenadas geográficas, registros fixos, ou como chaves em dicionários (desde que todos os seus elementos sejam imutáveis).