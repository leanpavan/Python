'''
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta
função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1
e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores
dentro da faixa de forma elegante.
'''


def retangulo(linhas,colunas):
    #Ajustar valor
    if linhas < 1:
        while linhas < 1:
            linhas += 1
    if colunas < 1:
        while colunas < 1:
            colunas += 1

    #Desenhar moldura
    print('+' + "-" * (colunas) + "+")

    for i in range(linhas - 2):
        print('|' + " " * (colunas) + '|')

    if linhas > 1:
        print('+' + "-" * (colunas) + "+")



linhas = int(input('Quantas linhas você deseja que o retangulo tenha?: '))
colunas = int(input("Quantas colunas você deseja que o retangulo tenha?: "))
retangulo(linhas,colunas)