'''endereco_puc = ("Rua Imaculada Conceição", "1555", "Prado Velho", "Curitiba", "PR")
um_item = ("Eu",)
tupla_vazia = tuple()
print(endereco_puc[0])
print(type(um_item))'''

enderecos = []
print("Cadastro de Endereços de Entrega")
while True:
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (logradouro, numero, bairro, cidade, estado)
    enderecos.append(novo_endereco)
    if input("Deseja cadastrar um novo endereço (s/n): ") == 'n':
        break
print("Os endereços cadastrados são:")
for i in range(len(enderecos)):
    endereco = enderecos[i]
    print(f"{i}, {endereco[0]}, {endereco[1]}, {endereco[2]}, {endereco[3]}, {endereco[4]}")