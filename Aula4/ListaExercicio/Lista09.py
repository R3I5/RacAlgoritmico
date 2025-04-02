# Escreva um programa que solicite o salario anual de uma pessoa e determine a aliquota de imposto de renda que se aplica. As aliquotas são: 0% para salario até R$ 20.000
# 15% para salário entre R$ 20.001 e R$ 50.000, e 25% para salário acima de R$ 50.000

salario = float(input('Insira seu salário anual:'))

if salario < 20000:
    aliquota = 0
elif 20000 <= salario < 50000:
    aliquota = 0.15
elif 50000 <= salario:
    aliquota = 0.25

ir = salario * aliquota
salarioFinal = salario - ir

print(f'Você deve pagar: {ir} R$ de imposto. Seu salário final é {salarioFinal}')
