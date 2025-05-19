# Criar um programa que cadastre funcionário de uma empresa e seus dependendetes.
# O funcinário deve ser cadastrado com matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla

cadastros = []
print(" Cadastro de funcionário e dependentes")
while True:
    matrícula = int(input("Digita a sua matrícula: "))
    nome = input("Digite o seu nome: ")
    if input("Deseja adicionar um dependente? (s/n) ") == "s":
        dependentes = ()
        nomeDependente = input("Digite o nome do dependente: ")
        dependentes += (nomeDependente,)
        while True:
            if input("Deseja adicionar um novo dependente? (s/n) ") == "n":
                break
            else:
                nomeDependente = input("Digite o nome do dependente: ")
                dependentes += (nomeDependente,)
        novoCadastro = (matrícula,nome,dependentes)
        cadastros.append(novoCadastro)
    else:
        novoCadastro = (matrícula,nome)
        cadastros.append(novoCadastro)
    if input("Deseja fazer um novo cadastro? (s/n)") == "n":
        break
print("Os cadastros realizados são: ")
for i in range(0, len(cadastros)):
    cadastro = cadastros[i]
    print(f"{i+1}° - Matricula: {cadastro[0]}, Nome: {cadastro[1]}")
    
    if len(cadastro) > 2:
        print("Dependentes: ")
        for j in cadastro[2]:
            print(f"{j}")
    else:
        print("Sem dependentes")
    print()
            
