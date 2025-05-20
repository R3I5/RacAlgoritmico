# Escreva um programa que solicita a idade de uma pessoa e certifique se ela é maior de idade. Se for maior de idade, verifique se tem idade suficiente para obter a Carteira Nacional de Habilitação

idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você é maior de idade')
    if idade >= 21:
        print('Você pode tirar sua CNH!')
    else:
        print('Você ainda não pode tirar sua CNH')
else:
    print('Você é menor de idade')