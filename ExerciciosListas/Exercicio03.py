# Faça um programa que leia 4 notas, mostre as notas e média na tela

vetor = []
for i in range(4):
    notas = float(input(f'Digite a {i+1}° nota do aluno:'))
    vetor.append(notas)
média = (sum(vetor)/4)
print(f'As notas do aluno foram: {vetor}')
print(f'A média do aluno foi: {média:.2f}')