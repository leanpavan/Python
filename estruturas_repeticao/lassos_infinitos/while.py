while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor Inválido")
print("Número válido: ", num)
