'''
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima
linha
'''
def imprimir(n):
    for i in range(1, n+1):
        string = ' '.join([str(i)] * i)
        print(string)


num = int(input("Digite um número para imprimir (-1 para parar): "))
imprimir(num)