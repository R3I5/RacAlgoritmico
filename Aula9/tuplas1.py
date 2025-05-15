# TUplas possuem estrutura muito parecidas com listas, sendo a principal diferença o fato das tuplas serem estruturas imutáveis
# ou seja, uma vez definido o seu conteúdo o mesmo não pode ser modificado
# Ex:

"""
Estrutura:
enderecoPuc = ("Rua Imaculada Conceição", 1555, "Padro velho", "Curitiba", "PR")
documentosJoão = ("13932007-1", "144593149-40")
tuplaVazia = tuple()
Exemplo: 
"""

enderecos = []
print("Cadastro de endereços de entrega")
while True:
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novoEndereco = (logradouro,numero,bairro,cidade,estado)
    enderecos.append(novoEndereco)
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
print("Os endereços cadastrados são: ")
for i in range(0, len(enderecos)):
    endereco = enderecos[i]
    print(f"{i}, {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")
