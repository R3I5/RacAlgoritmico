# Foram anotadas as idades e alturas dem 30 alunos.
# Faça um programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos

listaIdade = []
listaAltura = []
baixinhos = 0

for a in range(5):
    idades = int(input(f'Insira a idade do aluno {a+1}: '))
    listaIdade.append(idades)
    alturas = float(input(f'Insira a altura do aluno {a+1}: '))
    listaAltura.append(alturas)
    
media = (sum(listaAltura)/5)

for i in range(5):
    if listaIdade[i]>13 and listaAltura[i] < media:
        baixinhos += 1

print(f'A média de altura é: {media:.2f}')
print(f'Alunos abaixo da média de altura e acima de 13 anos: {baixinhos}')