"""
Tabuada de um numero especifico:
Solicite ao usuário um número inteiro. Após isso imprima a tabuada correspondente a esse número de 1 a 10 utilizando um loop for()
"""

try:
    numero = int(input('Digite um numero inteiro para obter a tabuada desejada: '))
    aux = 0
    while (aux < 10):
        aux = aux+1
        print(numero * aux)

except:
    print('Esse numero não é válido')
