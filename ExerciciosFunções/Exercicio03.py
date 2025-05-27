# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos

def soma(a,b,c):
    total = a+b+c
    return total
    
valor = []
for i in range(3):
    numero = int(input('Digite um numero:'))
    valor.append(numero)
final = soma(valor[0],valor[1],valor[2])
print(final)
