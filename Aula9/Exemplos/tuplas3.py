# Elaborar um programa que concatene tuplas.abs

enderecoPuc = ("Rua Imaculada Conceição", 1555, "Padro velho", "Curitiba", "PR")
print(id(enderecoPuc))
enderecoPuc += ("Brazil",)
print(enderecoPuc)
print(id(enderecoPuc))

# ao realizar a concatenação a tupla não é alterada,
# mas é na verdade criada uma nova tulpla, com o conteudo da antiga e o novo conteudo, recebendo um id diferente