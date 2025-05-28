"""
Sistema de Cadastro de Usuarios
"""

def showMenu(menu):
    print("*** Meu Sistema Querido***")
    for item in menu:
        print(item)
        
def getUserOption():
    pass

def userEdit():
    pass

def userCad():
    pass

def userRemove():
    pass

def userList(users: dict):
    print("*** Usuarios cadastrados ***")
    for cpf in users:
        print(f"CPF:",{cpf})
        user = users[cpf]
        print(f"Nome: {user['nome']}")
        print(f"Idade: {user['idade']}")
        print(f"Cidade: {user['cidade']}\n")
    print("*** Fim da Listagem ***")
    pass
        

def sistema(menu, users):
    while True:
        showMenu(menu)
        op = getIntOptioin('Opção: ')
        if op == 1:
            userCad()
        elif op == 2:
            userEdit()
        elif op == 3():
            userRemove()
        elif op == 4():
            userList()
        elif op == 5():
            print("Opção Inválida!!")
    
    def getIntOptioin(msg):
        while True: 
            try:
                op = int(input(msg))
                if op >= min and op <= max:
                    return op
                else:
                    print(f"Escolha uma opção entre {min} and {max}")
            except:
                print("Opção Inválida!!")
        
    pass




menuDoSistema = (
    "Cadastrar Usuário",
    "Editar Usuário",
    "Remover Usuário",
    "Listar Usuário",
    
)

usersDict = {
    {
        "14459314940":
            {
        "nome": "João",
        "idade": 20,
        "cidade": "Curitiba"
            }
    },
    {
        "123456789":
            {
        "nome": "Pedro",
        "idade": 35,
        "cidade": "Colombo"
            }
    }
            }

showMenu