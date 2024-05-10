'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa
deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma
para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para
P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua
um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''


def converter_notacao(horas, minutos):
    if horas == 0:
        horas_12 = 00
        periodo = "A"
    elif horas < 12:
        horas_12 = horas
        periodo = "A"
    elif horas == 12:
        horas_12 = 12
        periodo = "P"
    else:
        horas_12 = horas - 12
        periodo = "P"
    return horas_12, minutos, periodo


def print_horas(horas, minutos, periodo):
    if minutos < 10:
        minutos_str = f"0{minutos}"
    else:
        minutos_str = f"{minutos}"

    print(f"{horas}:{minutos_str} {periodo}M")


input_horas = int(input("Informe a hora: "))
input_minutos = int(input("Informe os minutos: "))
horas_12, minutos, periodo = converter_notacao(input_horas, input_minutos)
print_horas(horas_12, minutos, periodo)