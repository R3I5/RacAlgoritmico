# 2. Manipulação de Dicionários (Exemplo: Estoque)
# A tarefa de atualizar a quantidade de um item no dicionário é comum.

# Python

estoque = {}

def adicionar_item_estoque(nome_item, quantidade, meu_estoque):
    if nome_item in meu_estoque:
        meu_estoque[nome_item] += quantidade
        print(f"Estoque de '{nome_item}' atualizado para {meu_estoque[nome_item]} unidades.")
    else:
        meu_estoque[nome_item] = quantidade
        print(f"Item '{nome_item}' adicionado com {quantidade} unidades.")
    return meu_estoque

estoque = adicionar_item_estoque("maçã", 10, estoque)
# Saída: Item 'maçã' adicionado com 10 unidades.
estoque = adicionar_item_estoque("banana", 5, estoque)
# Saída: Item 'banana' adicionado com 5 unidades.
estoque = adicionar_item_estoque("maçã", 3, estoque)
# Saída: Estoque de 'maçã' atualizado para 13 unidades.
print(f"Estoque final: {estoque}")
# Saída: Estoque final: {'maçã': 13, 'banana': 5}