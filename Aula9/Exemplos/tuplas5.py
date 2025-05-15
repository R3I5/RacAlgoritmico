# Elaborar um programa que faça uso de uma tupla chamada Endereco, contendo dados nomeados

from collections import namedtuple

endereco = namedtuple("Endereco", ["logradouro", "numero","bairro", "cidade", "estado"])
enderecoPuc = endereco(logradouro="Rua Imaculdada Conceição", numero=1555, bairro="Prado Velho", cidade="Curitiba", estado="PR")
print(f"Endereço: {enderecoPuc[0]}")
print(f" Número: {enderecoPuc.numero}")
print(f" Bairro: {enderecoPuc.bairro}")
print(f" Cidade: {enderecoPuc.cidade}")
print(f" Estado: {enderecoPuc.estado}")