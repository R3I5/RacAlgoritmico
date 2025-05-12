# Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida

altura = []
idade = []
for i in range(5):
    idadePessoa = float(input(f'Insira a idade da {i+1}° pessoa: '))
    idade.append(idadePessoa)
    alturaPessoa = float(input(f'Insira a altura da {i+1}° pessoa: '))
    altura.append(alturaPessoa)
    
print(f'Altura: {altura}')
print(f'Idade: {idade}')