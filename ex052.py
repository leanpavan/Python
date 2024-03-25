'''5. Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:
Condição Ida Ida e volta
Região Norte R$ 500,00 R$ 900,00
Região Nordeste R$ 350,00 R$ 650,00
Região Centro-Oeste R$ 350,00 R$ 600,00
Região Sul R$ 300,00 R$ 550,00
'''

def calcular_precos_passagem(destino, ida_e_volta):
    precos = {
        "norte": {"ida": 500, "ida_e_volta": 900},
        "nordeste": {"ida": 350, "ida_e_volta": 650},
        "centro-oeste": {"ida": 350, "ida_e_volta": 600},
        "sul": {"ida": 300, "ida_e_volta": 550}
    }

    destino = destino.lower()

    if destino in precos:
        if ida_e_volta:
            return precos[destino]["ida_e_volta"]
        else:
            return precos[destino]["ida"]
    else:
        return "Destino inválido!"


print("Bem-vindo ao sistema de cálculo de preço de passagem!")
destino = input("Por favor, informe o destino da viagem (Norte, Nordeste, Centro-Oeste ou Sul): ")
ida_e_volta = input("A viagem inclui retorno? (S/N): ")

if ida_e_volta.upper() == "S":
    ida_e_volta = True
else:
    ida_e_volta = False

preco = calcular_precos_passagem(destino, ida_e_volta)

if type(preco) == int:
    print(f"O preço da passagem para {destino.capitalize()} {'ida e volta' if ida_e_volta else 'ida'} é R${preco},00.")
else:
    print(preco)

