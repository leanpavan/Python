'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um
item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''


def somaImposto(taxaImposto, custo):
    custo += taxaImposto / 100
    return custo


taxa = int(input("Digite a taxa do imposto em porcentagem: "))
valor = int(input("Digite o custo do item: "))
custo = somaImposto(taxa, valor)
print(f"O valor com o imposto incluso é: R${custo}")