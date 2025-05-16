# Criar um programa que efetua o cadastro de pessoas com nome, rg e cpf por meio de tuplas
# Adicionando elas a uma lista. Imprimir a lista ao final do programa

cadastros = []
print(" Cadastro de pessoa ***")
while True:
    nome = input("Digite o seu nome: ")
    rg = input("Digite o seu rg: ")
    cpf = input("Digite o seu cpf: ")
    novoCadastro = (nome,rg,cpf)
    cadastros.append(novoCadastro)
    if input("Deseja fazer um novo cadastro? (s/n): ") == "n":
        break
print("Os cadastros realizados são: ")
for i in range(0, len(cadastros)):
    cadastro = cadastros[i]
    print(f"{i+1}°, {cadastro[0]}, {cadastro[1]}, {cadastro[2]}")
    
            