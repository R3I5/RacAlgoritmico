# A matriz identidade é uma matriz de mesma quantidade de linhas e colunas que tem todos os elementos da diagonal principal
# (de cima para baixo, esquerda para direita) iguais a 1, e demais elementos iguais a 0. 
# Criar um programa que solicita o tamanho da matriz desejada, que gera a matriz identidade.

tamanho = int(input('Insira o tamanho da matriz desejada: '))
matriz = []
for i in range (tamanho):
    linha = []
    for j in range (tamanho):
        linha.append(0)
    matriz.append(linha)
for posição in range (tamanho):
    matriz[posição][posição] = 1
for linha in matriz:
    print(linha)

