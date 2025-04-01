#Escreva um programa que solicite ao usuário o salário atual e o tempo de serviço em anos. Se o tempo de serviço for superior a 5 anos
#Concede um bônus de 5% sobre o salário. Caso contrário, não conceda bônus

salario = float(input('Insira o valor do salário: '))
bonus = salario*0.05
tempo = int(input('Insira o valor do serviço em anos: '))
if tempo > 5:
    salarioFinal = salario + bonus
    print(f'Parabéns! Você recebeu um bonus de {bonus} R$, seu salário agora é: {salarioFinal} R$')
else:
    print('Sem bônus por enquanto')
