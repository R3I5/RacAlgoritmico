# Elaborar um programa que simule o cadastro de telefones com dicionário como uma agenda
# Caso seja de um nome já existente, perguntar se deseja alterar dados existentes.
# Caso seja um telefone já existente, informar que este telefone já esta cadastrado em outro contato, não podendo ser efetuada a inclusão. Ao final, exiba o dicionário

agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if contato in agenda:
        if input(f"Contato já esta cadastrado com o número {agenda[contato]}. Deseja alterar (s/n) ") == "n":
            continue
    if telefone in agenda.values():
        print("Telefone já esta cadastrado para outro contato")
        continue
    agenda[contato] = telefone
    if input("Deseja cadastrar um novo contato (s/n) ") == "n":
        break
print(agenda)