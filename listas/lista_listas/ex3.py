# Criar um programa que lê as temperaturas médias de cada mês
# do ano e as armazena em uma lista. Usar um outro vetor para
# guardar e exibir, quando necessário, os nomes dos meses do ano.
# Calcular a média anual de temperatura, e informar quais meses
# ficaram acima desta média anual.

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = []
aux = []

for mes in meses:
    temp = int(input(f"temperatura média de {mes}: "))
    temperaturas.append(temp)

media_temp = sum(temperaturas) / len(temperaturas)

acima_media = []
for i in range(len(temperaturas)):
    if temperaturas[i] > media_temp:
        acima_media.append(temperaturas[i])

print(f"A média anual de temperatura é: {media_temp:.2f}")

print(f"\nOs meses que ficaram acima da média de temperatura foram: ")
for i in range(len(temperaturas)):
    if temperaturas[i] > media_temp:
        aux.append((meses[i], temperaturas[i]))

    print(f"{aux}")