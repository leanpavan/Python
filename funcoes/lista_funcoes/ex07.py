'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de
uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá
voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a
prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para
pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
juros por dia de atraso.
'''
quantidade_prestacoes = 0
valor_final = 0


def valorPagamento(prestacao, dias_atraso):
    multa = 0.03
    juros = 0.001
    valor_total = prestacao

    if dias_atraso > 0:
        valor_total += prestacao * multa
        valor_total += prestacao * (juros * dias_atraso)
    return valor_total


while True:
    prestacao = float(input("Qual o valor da prestação? (0 - Finalizar): "))
    if prestacao == 0:
        break
    dias_atraso = int(input("Quantos dias de atraso? "))
    valor_total = valorPagamento(prestacao, dias_atraso)
    print(f"Valor a ser pago: R${valor_total:.2f}")
    quantidade_prestacoes += 1
    valor_final += valor_total

print(f"\nRelatório diário:")
print(f"\nQuantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total pago: {valor_final}")