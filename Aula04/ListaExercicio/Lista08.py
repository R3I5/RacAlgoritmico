# Escreva um programa que solicita a nota de um aluno em uma prova e determine sua classificação. A(nota de 9  10), B(nota de 7 a 8.9), C(nota de 5 a 6.9) ou D(nota abaixo de 5)

nota = float(input('Insira a nota da prova:'))
if nota < 5:
    print('Conceito D, Aluno Reprovado')
elif 5 <= nota < 7:
    print('Conceito C, Aluno em Recuperação')
elif 7 <= nota < 9:
    print('Conceito B, Aluno Aprovado')
else:
    print('Conceito A, Aluno Aprovado')