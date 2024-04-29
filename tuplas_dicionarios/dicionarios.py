faturamento = {"janeiro": 2000, "fevereiro": 3500, "março": 2800}

faturamento_janeiro = faturamento["janeiro"]
print(faturamento_janeiro)

faturamento["janeiro"] = 5000

people = {}
while True:
    name = input("Digite o nome da pessoa: ")
    cpf = input("Digite o CPF da pessoa: ")
    if cpf in people:
        if input("CPF já cadastrado. Deseja alterar os dados (s/n)") == 'n':
            continue
    people[cpf] = name
    if input("Deseja continuar (s/n): ") == 'n':
        break
print(people)