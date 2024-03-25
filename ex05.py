'''
5. Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:
Condição Ida Ida e volta
Região Norte R$ 500,00 R$ 900,00
Região Nordeste R$ 350,00 R$ 650,00
Região Centro-Oeste R$ 350,00 R$ 600,00
Região Sul R$ 300,00 R$ 550,00
'''

destino = input("Selecione a região que deseja viajar (Norte, Nordeste, Centro-Oeste, Sul): ")
passagem = int(input("Escolha se deseja passagem só de ida ou ida e volta (1 - Ida / 2 - Ida e Volta): "))




if destino.lower() == "norte":
    if passagem == 1:
        print("O destino escolhido foi a região Norte, com passagem só de ida no valor de R$500,00")
    else:
        print("O destino escolhido foi a região Norte, com passagem de ida e volta no valor de R$900,00")

if destino.lower() == "nordeste":
    if passagem == 1:
        print("O destino escolhido foi a região Nordeste, com passagem só de ida no valor de R$350,00")
    else:
        print("O destino escolhido foi a região Nordeste, com passagem de ida e volta no valor de R$650,00")

if destino.lower() == "centro-oeste":
    if passagem == 1:
        print("O destino escolhido foi a região Centro-Oeste, com passagem só de ida no valor de R$300,00")
    else:
        print("O destino escolhido foi a região Centro-Oeste, com passagem de ida e volta no valor de R$600,00")

if destino.lower() == "sul":
    if passagem == 1:
        print("O destino escolhido foi a região Sul, com passagem só de ida no valor de R$350,00")
    else:
        print("O destino escolhido foi a região Sul, com passagem de ida e volta no valor de R$550,00")