"""
Soma dos números pares até um limite:
Peça ao usuario para inserir um numero inteiro positivo. Em seguida, some todos os números pares até esse limite usando um loop
"""
numero = int(input('Insira um número inteiro positivo: '))

if numero < 0:
    print('Por favor, insira um número válido.')
else:
    soma = 0
    x = 0
    while x <= numero:
        if x % 2 == 0:
            soma += x
        x += 1  # incrementa de 1 em 1
    print('A soma dos números pares até', numero, 'é:', soma)
