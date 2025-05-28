# 5. Estruturas de Dados Aninhadas (Exemplo: Cadastro de Usuário)
# Dicionários podem conter outros dicionários ou listas como valores, criando estruturas complexas.

# Python

usuarios_cadastrados = {} # Dicionário principal para armazenar todos os usuários

def cadastrar_novo_usuario(id_usr, nome_usr, email_usr, lista_habilidades, bd_usuarios):
    """Cadastra ou atualiza um usuário no banco de dados (dicionário)."""
    bd_usuarios[id_usr] = {
        'dados_pessoais': {
            'nome': nome_usr,
            'email': email_usr
        },
        'habilidades_tecnicas': lista_habilidades
    }
    print(f"Usuário {id_usr} ({nome_usr}) cadastrado/atualizado.")
    # print(f"Dados: {bd_usuarios[id_usr]}") # Para ver o registro específico
    return bd_usuarios

# Cadastrando o primeiro usuário
usuarios_cadastrados = cadastrar_novo_usuario(
    id_usr=101,
    nome_usr="Alice Wonderland",
    email_usr="alice@example.com",
    lista_habilidades=["Python", "Comunicação", "Chá"],
    bd_usuarios=usuarios_cadastrados
)

# Cadastrando o segundo usuário
usuarios_cadastrados = cadastrar_novo_usuario(
    id_usr=102,
    nome_usr="Bob The Builder",
    email_usr="bob@example.com",
    lista_habilidades=["Construção", "Ferramentas", "Trabalho em equipe"],
    bd_usuarios=usuarios_cadastrados
)

# Atualizando o primeiro usuário (mesmo ID)
usuarios_cadastrados = cadastrar_novo_usuario(
    id_usr=101,
    nome_usr="Alice W. Updated",
    email_usr="alice.updated@example.com",
    lista_habilidades=["Python", "Comunicação Avançada", "Chá com Biscoitos", "Lógica"],
    bd_usuarios=usuarios_cadastrados
)

print("\nBanco de dados de usuários final:")
for user_id, user_data in usuarios_cadastrados.items():
    print(f"ID: {user_id}")
    print(f"  Nome: {user_data['dados_pessoais']['nome']}")
    print(f"  Email: {user_data['dados_pessoais']['email']}")
    print(f"  Habilidades: {', '.join(user_data['habilidades_tecnicas'])}")

# Acessando um dado específico:
# print(f"\nEmail da Alice: {usuarios_cadastrados[101]['dados_pessoais']['email']}")
# print(f"Primeira habilidade do Bob: {usuarios_cadastrados[102]['habilidades_tecnicas'][0]}")