"""
2. Manipulação de Dicionários: Atualização de Estoque
Questão para estudo: Crie um programa em Python que simule o controle de estoque de uma pequena loja.
a) Inicie com um dicionário vazio chamado estoque.
b) Crie uma função chamada adicionar_item(nome_item, quantidade) que: Se o nome_item já existir no estoque, some a quantidade informada à quantidade existente.
Se o nome_item não existir, adicione-o ao estoque com a quantidade informada.
A função deve imprimimr uma mensagem confirmando a operação (ex: "5 unidades do item 'Maçã' adicionadas")
c) Teste sua função adicinonando e atualizando alguns itens. Por exemplo:
Adicionar "Maçã", 10 unidades
Adicionar "Banana", 5 unidades
Adicionar "Maçã", 3 unidades(deve atualizar a quantidade de maçãs para 13)
d) Ao final, imprima o dicionário estoque completo
"""
# Resposta: 

estoque = {}

def adicionarItem(nomeItem, quantidade, meuEstoque):
    if nomeItem in estoque:
        meuEstoque[nomeItem] += quantidade
        print(f"Estoque de '{nomeItem}' atualizado para {meuEstoque[nomeItem]} unidades.")
    else:
        estoque[nomeItem] = quantidade
        print(f"Item '{nomeItem}' adicionado com {quantidade} unidades. ")
    return meuEstoque

print("*** Atualização de Estoque ***")
while True:
    item = input("Qual item você deseja adicionar? ")
    nmr = int(input("Quantos itens vão ser adicionados? "))
    adicionarItem(item,nmr,estoque)
    print(f"Estoque final: {estoque}")
    if input("Deseja adicionar algo a mais?: (s/n) ") == 'n':
        print("Obrigador por utilizar nosso programa!")
        break

    pass