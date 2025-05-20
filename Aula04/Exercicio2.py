nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1+nota2)/2
if media >= 7.0:
    print('Aprovado')
elif media >= 5.0:
    print('Em recuperação')
else:
    print('Reprovado')