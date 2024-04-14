# Criar um programa que simula um carrinho de compras, onde
# solicita o nome do produto (não pode ser vazio), o valor deste
# produto (valor com vírgula, positivo) e a quantidade deste
# produto a ser comprada (valor inteiro, positivo). Ao incluir um
# produto, deve perguntar se o usuário deseja fechar o pedido ou
# incluir mais produtos. Todos os dados devem ser validados. Ao
# final da compra, deve ser informado o valor total do pedido.

#Database do mercado
itens_precos = {
    "Maçãs (1 kg)": 5.00,
    "Arroz (5 kg)": 10.00,
    "Feijão (1 kg)": 6.50,
    "Frango (1 kg)": 8.00,
    "Leite (1 litro)": 3.50,
    "Pão de forma (500g)": 4.00,
    "Tomates (1 kg)": 4.50,
    "Batatas (1 kg)": 3.00,
    "Ovos (dúzia)": 6.00,
    "Cenouras (1 kg)": 2.50
}

for item, preco in itens_precos.items():
    print(f"{item}: R${preco:.2f}")

quebrador = False

while not quebrador:
    nome_produto = input(f"\nForneça o nome do produto: ")
    if nome_produto == "":
        continue
    else:
        if nome_produto in itens_precos:
            preco = itens_precos[nome_produto]