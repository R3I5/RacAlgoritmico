# Dicionários (Dictionaries)
# O que são? Coleções não ordenadas (em Python < 3.7) ou ordenadas por inserção (Python 3.7+) de pares chave: valor. São mutáveis. Cada chave deve ser única e imutável (ex: strings, números, tuplas com itens imutáveis).
# Sintaxe: Definidos por chaves {}, com pares chave: valor separados por vírgulas.
# Exemplos:
# Python

# Criação
aluno = {"nome": "João", "idade": 20, "curso": "Engenharia"}
estoque = {"maçã": 10, "banana": 15}

# Acessando valores pela chave
print(aluno["nome"])      # Saída: João
print(estoque.get("laranja", 0)) # Saída: 0 (get evita erro se a chave não existe)

# Modificando/Adicionando valores
aluno["idade"] = 21
aluno["cidade"] = "São Paulo" # Nova chave-valor adicionada
print(aluno)
# Saída: {'nome': 'João', 'idade': 21, 'curso': 'Engenharia', 'cidade': 'São Paulo'}

# Removendo itens
del aluno["curso"]
print(aluno)
# Saída: {'nome': 'João', 'idade': 21, 'cidade': 'São Paulo'}
quantidade_banana = estoque.pop("banana")
print(quantidade_banana) # Saída: 15
print(estoque)           # Saída: {'maçã': 10}

# Iterando sobre chaves, valores ou itens
for chave in aluno.keys():
    print(chave)
for valor in aluno.values():
    print(valor)
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
# Uso comum: Para representar objetos do mundo real (como um cadastro de usuário), para contar frequências, ou quando você precisa acessar valores rapidamente através de um identificador único (a chave).