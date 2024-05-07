def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial(num - 1)


n = int(input("Digite o número que deseja calcular o fatorial: "))
fat = fatorial(n)
print(f"O fatorial de {n} é {fat}")