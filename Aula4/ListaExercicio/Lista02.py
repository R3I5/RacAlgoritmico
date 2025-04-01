# Escreva um programa que leia um número inteiro e determine se ele é positivo, negativo ou zero

numero = float(input('Insira o número:'))
if numero == 0:
    print('O número é igual a 0')
elif numero > 0: 
    print('O número é positivo')
else:
    print('O número é negativo')