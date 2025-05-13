# Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida

altura = []
idade = []

alturaInversa = []
idadeInversa = []

for i in range(2):
    idadePessoa = int(input(f'Insira a idade da {i+1}° pessoa: '))
    idade.append(idadePessoa)
    alturaPessoa = float(input(f'Insira a altura da {i+1}° pessoa: '))
    altura.append(alturaPessoa)
    
alturaInversa = list(reversed(altura))
idadeInversa = list(reversed(idade))

print(f'Idade: {idade}')
print(f'Altura: {altura}')

print(f'Idade inversa: {idadeInversa}')
print(f'Altura inversa: {alturaInversa}')
