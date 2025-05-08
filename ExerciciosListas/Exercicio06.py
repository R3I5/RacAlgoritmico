# Faça um programa que peça as quatro notas de 10 alunos. calcule e armazene num vetor a média de cada aluno
# Imprima o número de alunos com média maior ou igual a 7.0

alunos = []
medias = []
qtdAlunos = 0

for i in range(10):
    nome = input(f'Insira o nome do {i+1}° aluno: ')
    alunos.append(nome)
    
    notas = []
    for i in range(4):
        nota = float(input(f'Insira a nota {i+1}° do aluno: '))
        notas.append(nota)
        
    média = ((sum(notas))/4)
    medias.append(média)
    print(f'A média do aluno {nome} é: {média:.2f} \n')
    
    if média >= 7.0:
        qtdAlunos = qtdAlunos + 1
print(f'Os nomes dos alunos são: {alunos} ')
print(f'{qtdAlunos} ficaram com nota acima de 7.0')