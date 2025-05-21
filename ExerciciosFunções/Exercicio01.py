# Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3
# . . . . . .
# n n n n n n n n n n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha

def criarLinhas(linhas):
    resultado = []
    linha = 0
    for i in range(linhas):
        linha = linha + 1
        resultado.append((str(linha) + ' ') * linha)
    return resultado

n = int(input("Digite o número de linhas desejadas: "))
linhasGeradas = criarLinhas(n)

for linha in linhasGeradas:
    print(linha)


