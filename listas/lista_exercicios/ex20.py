'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato
laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será
de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste
momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa,
descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um
número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após
a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de
acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins
ilustrativos. Os valores podem mudar a cada execução do programa.
'''

salario_bruto = []
salario_funcionarios = []
total_abonos = []
aux = 0

while True:
    salario = int(input("Digite o salário do funcionário (0-Finalizar): "))
    if salario == 0:
        break
    salario_bruto.append(salario)

for s in salario_bruto:
    abono = s * 0.20
    if abono < 100:
        abono = 100
        aux += 1
    salario_total = s + abono
    total_abonos.append(abono)
    salario_funcionarios.append(salario_total)

print(salario_bruto)
print(f"{salario_funcionarios}\n")

print("Projeção de Gastos com Abono")
print(f"============================\n")
for i in salario_bruto:
    print(f"Salário: {i:.2f}\n")

print(f"Salário         -            Abono")
for c in range(len(salario_bruto)):
    print(f"R${salario_bruto[c]:>7.2f}       -       R$ {total_abonos[c]:>7.2f}")

print(f"\nForam processados {len(salario_bruto)+1} colaboradores")
print(f"Total gasto com abonos: R$ {sum(total_abonos):.2f}")
print(f"Valor mínimo pago a {aux} colaboradores")
print(f"Maior valor de abono pago: R$ {max(total_abonos):.2f}")
