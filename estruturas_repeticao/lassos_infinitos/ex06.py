'''Criar um programa que pede para o usuário inserir um login e uma
senha. Caso os valores sejam iguais, informar que os dados são
inválidos e pedir novamente as informações. Caso contrário, exibir a
mensagem "Bem-vindo ao sistema!!!".
'''

while True:
    try:
        login = input("Login: ")
        senha = int(input("Senha: "))
        if login == str(senha):
            print("Dados inválidos")
        else:
            print("Bem-vindo ao Sistema!")
            break
    except:
        print("Dados inválidos")