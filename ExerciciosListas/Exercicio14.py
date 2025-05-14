# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vitima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vitima?"
# d. "Devia para a vitima?"
# e. "Ja trabalhou com a vitima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como "Suspeita" entre 3 e 4 como "Cumplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"

perguntas = ['Telefonou para a vitima? ',
            'Esteve no local do crime? ',
            'Mora perto da vitima? ',
            'Devia para a vitima? ',
            'Ja trabalhou com a vitima? '
            ]
respostas = 0

print('Por favor, responda as seguintes perguntas com "Sim" ou "Não"')

for i, pergunta in enumerate(perguntas): #transfere a posição i para a pergunta
    resposta = input(pergunta)
    if resposta == 'Sim' or resposta == 'sim' or resposta == 's' or resposta == 'S':
        respostas += 1
    elif resposta == 'Não' or resposta == 'Nao' or resposta == 'não' or resposta == 'nao' or resposta == 'N' or resposta == 'n':
        respostas += 0

if respostas == 2:
    print('Você é suspeito!')
elif respostas == 3 or respostas == 4:
    print('Você é cúmplice!')
elif respostas == 5:
    print('Você é o assassino!')
else:
    print('Você é inocente!')
    
