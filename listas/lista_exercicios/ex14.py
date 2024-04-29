'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente".'''

sim = []
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

print(f"Interrogatório\n")
print(f'Digite S-SIM e N-NÃO\n')
for p in perguntas:
    resp = input(p).upper()
    print(resp)
    if resp == 'S':
        sim.append(resp)

if len(sim) == 2:
    print('Suspeito')
elif len(sim) >= 3 and len(sim) <= 4:
    print('Cúmplice')
elif len(sim) == 5:
    print('Assasino')
else:
    print("Inocente")