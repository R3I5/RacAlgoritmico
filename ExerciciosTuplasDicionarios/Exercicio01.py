# 1. Restaurante Boca Feliz

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}

# Imprimir o cardápio do restaurante com as opções de produtos ofertados;

while True:
    print("Bem-Vindo ao Restaurante Boca Feliz!!")
    print(" Cardapio ")
    for produto in cardapio:
        print(produto)

# Logo abaixo do cardapio, exibir a mensagem "O que deseja pedir (0 para sair)?"

    pedido = input("O que deseja pedir? (0 para sair)")
    
# Digitando "0" deve sair do programa
    
    if pedido == "0":
        print("Obrigado e volte sempre!")
        break
    
# Digitando o nome do produto pode ter uma das seguintes possibilidades:
# Se o item não consta no cardapio exibir a mensagem "item não localizado no caradpio";

    elif pedido not in cardapio:
        print("Item não localizado no cardápio")
    else:

# Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma mensagem para cada ingrediente faltante

        ingredientes = cardapio[pedido] 
        vender = True   
        for ingrediente in ingredientes:
            if estoque[ingrediente] <= 0:
                print(f"Infelizmente acabou o {ingrediente}")
                vender = False
        if vender:
            print(f" Um {pedido} saindo no capricho!")
            for ingrediente in ingredientes:
                estoque[ingrediente] -= 1
            