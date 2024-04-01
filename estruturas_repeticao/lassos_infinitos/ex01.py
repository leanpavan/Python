while True:
    try:
        num = int(input("Digite um número de 1 a 5: "))
        if num < 5 and num >= 1:
            break
        else:
            print("Range inválido: entrar número entre 1 e 5")
    except:
        print("Entrada inválida")

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")