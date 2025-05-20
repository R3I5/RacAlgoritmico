# Escreva um programa que solicite a idade de uma pessoa e determine em qual categoria ela se encaixa: criança(0-12 anos), adolescente(13 - 17 anos), adulto(18-59 anos) ou idoso (60 anos ou mais)

idade = int(input('Insira sua idade: '))
if 0 < idade <= 12:
    print('Você é criança')
elif 13 <= idade <= 17:
    print('Você é adolescente')
elif 18 <= idade <= 59:
    print('Você é adulto')
elif idade>=60:
    print('Você é idoso')
else:
    print('Idade inválida')