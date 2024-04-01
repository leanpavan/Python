'''Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
• para homens: (72.7 * h) – 58;
• para mulheres: (62.1 * h) – 44.7.'''

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo biológico (masculino/feminino): ")

if sexo.lower() == "masculino":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f"O peso ideal para o sexo {sexo} e altura {altura}cm é {peso_ideal}kg")