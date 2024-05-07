agenda_telefonica = {}


def inserir(nome, telefone, agenda):
    if nome in agenda:
        if input("Contato já existe, deseja alterar este telefone? (S/N): ").upper() == 'N':
            return False
        agenda[nome] = telefone
        return True

while True:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if inserir(nome, telefone, agenda):
        print("Contato adicionado com sucesso!")
    else:
        print("Falha ao tentar adicionar contato.")