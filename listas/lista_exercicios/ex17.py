'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo:
'''
saltos = []
while True:
    atleta = input('Digite o nome do atleta: ')
    if atleta == '':
        break
    else:
        for i in range(5):
            salto = float(input(f'Digite o valor do {i+1}º salto: '))
            saltos.append(salto)
        break

media_saltos = sum(saltos) / len(saltos)
print(f"\n Atleta: {atleta}\n")

print(f"Primeiro Salto: {saltos[0]} m")
print(f"Segundo Salto: {saltos[1]} m")
print(f"Terceiro Salto: {saltos[2]} m")
print(f"Quarto Salto: {saltos[3]} m")
print(f"Quinto Salto: {saltos[4]} m")

print(f"\nResultado Final:")

print(f"\nAtleta: {atleta}")
print(f"Saltos: {saltos}")
print(f"Média dos saltos: {media_saltos} m")