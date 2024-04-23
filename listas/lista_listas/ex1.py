# Criar um programa que solicita ao usuário 6 números, calculando
# sua média. Mostrar ao usuário uma lista com os números iguais
# ou acima da média e uma lista com os números abaixo da média.

nums = []
for _ in range(6):
    num = int(input("bota um num ae: "))
    nums.append(num)

avg = sum(nums) / len(nums)
nums_up = []
nums_down = []
for num in nums:
    if num >= avg:
        nums_up.append(num)
    else:
        nums_down.append(num)

print(f"\nMédia: {avg}")
print(f"\nAcima ou igual a média😍😍: {nums_up} / Abaixo  da média😢😢: {nums_down}")