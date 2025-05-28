# 3. Funções e Conversão de Tipos (Lista para Dicionário)
# Funções ajudam a organizar e reutilizar código.

# Python

# Função para converter duas listas (chaves e valores) em um dicionário
def listas_para_dicionario(lista_chaves, lista_valores):
    novo_dicionario = {}
    # Garante que as listas tenham o mesmo tamanho para evitar erros
    # A função zip é uma forma mais elegante para isso, mas vamos fazer manualmente
    # para ilustrar o loop, como o exercício pode pedir.
    # zip(lista_chaves, lista_valores) criaria pares (chave, valor)
    min_len = min(len(lista_chaves), len(lista_valores)) # Para evitar IndexError

    for i in range(min_len):
        chave = lista_chaves[i]
        valor = lista_valores[i]
        novo_dicionario[chave] = valor # Se a chave se repetir, a última prevalecerá
    return novo_dicionario

nomes = ["Ana", "Bruno", "Carlos", "Ana"]
idades = [25, 30, 22, 28] # Ana aparece duas vezes

cadastro = listas_para_dicionario(nomes, idades)
print(cadastro)
# Saída: {'Ana': 28, 'Bruno': 30, 'Carlos': 22}
# A segunda ocorrência de "Ana" com idade 28 sobrescreveu a primeira.

# Usando zip (mais idiomático em Python):
def listas_para_dicionario_zip(lista_chaves, lista_valores):
    # Se chaves duplicadas, zip pega a primeira ocorrência para a chave
    # Para o comportamento do exercício (última prevalece), o loop anterior é melhor
    # ou criar o dicionário com um loop após o zip se for necessário
    return dict(zip(lista_chaves, lista_valores))

# Se a questão exigir que a ÚLTIMA ocorrência de uma chave duplicada prevaleça,
# o primeiro método (com loop e atribuição direta) é mais direto.