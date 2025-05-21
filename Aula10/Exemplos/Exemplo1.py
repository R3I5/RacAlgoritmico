# Elaborar um programa que cadastra contatos de agenda telefônica. A função de cadastro deve ser realizada dentro de uma função chamada inserir,
# Que recebe como parâmetros o nome e o telefone do contato, bem como a agenda de contatos

agendaTelefonica = {}

def inserir(nome, telefone, agenda):
    agenda[nome] = telefone
    
while True:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    inserir(nome, telefone, agendaTelefonica)
    if input("Gostaria de adicionar um novo contato? (s/n)") == "n":
        break
    
print(agendaTelefonica)