'''
Elaborar um programa que soma 10 números usando lassos
'''
soma = 0
for i in range(10):
    num = int(input("Digite o " + str(i + 1) + "º número: "))
    soma += num
print(f"A soma dos números é {soma}")