def piramide(n):
    aux = 1
    while aux < n+1:
        print(f"{aux} " * aux)
        aux += 1


n = int(input("Digite o tamanho da piramide: "))
piramide(n)
