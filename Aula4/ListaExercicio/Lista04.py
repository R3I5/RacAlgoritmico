#Escreva um programa que solicite ao usuário os três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno

lado1 = float(input('Informe o tamanho do primeiro lado do triângulo: '))
lado2 = float(input('Informe o tamanho do segundo lado do triângulo: '))
lado3 = float(input('Informe o tamanho do terceiro lado do triângulo: '))

if lado1 + lado2 == lado3:
    print('Tamanhos inválidos')
elif lado2 + lado3 == lado1:
    print('Tamanhos inválidos')
elif lado3 + lado1 == lado2:
    print('Tamanhos inválidos')
else:
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triângulo Isósceles')
    elif lado1 != lado2 or lado2 != lado3 or lado1 != lado3:
        print('Triângulo Escaleno')