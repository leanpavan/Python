'''
Criar um programa que, fazendo uso de funções, cadastra
contatos em uma agenda telefônica, podendo excluir estes
contatos. Deve ser exibido um menu com as opções: inserir,
remover e sair.
'''
agenda = {}


def inserir_agenda(nome, telefone):
    if nome in agenda:
        if input("Contato já existe na agenda, deseja atualizá-lo (S/N): ").upper() == "N":
            return False
    agenda[nome] = telefone
    return True


while True:
    nome = input("Digite o contato que deseja adicionar: ")
    telefone = input("Digite o telefone do contato: ")
    if inserir_agenda(nome, telefone):
        print("Contato adicionado com sucesso")
    else:
        print("Contato já existente")
