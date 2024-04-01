'''
4. Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.
Código Condição de pagamento
• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
• 2 – À vista no cartão de crédito, recebe 15% de desconto
• 3 – Em duas vezes, preço normal de etiqueta sem juros
• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%
'''

preco = float(input("Digite o preço do produto a ser adquirido: "))
valor_final = preco
desconto = 0

print("Forma de pagamento: ")
print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto ")
print("2 - À vista no cartão de crédito, recebe 15% de desconto ")
print("3 - Em duas vezes, preço normal de etiqueta sem juros ")
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10% ")

pagamento = int(input("Escolha a sua forma de pagamento de acordo com a tabela acima de 1 à 4: "))
if pagamento == 1:
    desconto = 0.10
    valor_final = valor_final - (valor_final * desconto)
    print(f"A forma de pagamento escolhida foi no dinheiro ou cheque com {desconto*100}% de desconto com valor final de: {valor_final:.2f}")
elif pagamento == 2:
    desconto = 0.15
    valor_final = valor_final - (valor_final * desconto)
    print(f"A forma de pagamento escolhida foi no cartão de crédito com {desconto*100}% de desconto com valor final de: {valor_final:.2f}")
elif pagamento == 3:
    print(f"O produto será pago em duas parcelas de {preco/2}R$ sem juros")
else:
    juros = 0.10
    parcela = preco/2
    valor_final = parcela + (preco * 0.10)
    print(f"O produto será pago em duas parcelas de {parcela:.2f}R$ e {valor_final:.2f}R$ com juros de 10% ao mês")


