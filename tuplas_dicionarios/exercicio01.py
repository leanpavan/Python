'''
Criar um programa que efetua o cadastro de pessoas com nome,
rg e cpf por meio de tuplas, adicionando elas a uma lista.
Imprimir a lista ao final do programa.
'''
lista = []
while True:
    nome = input("Digite um nome: ")
    rg = input("Digite um rg: ")
    cpf = input("Digite um cpf: ")
    tupla = (nome, rg, cpf)
    lista.append(tupla)
    if input("Deseja adicionar mais uma pessoa (S/N): ") == "n":
        break
for i in range(len(lista)):
    aux = lista[i]
    print(f"\nNOME: {aux[0]}")
    print(f"RG: {aux[1]}")
    print(f"CPF: {aux[2]}")