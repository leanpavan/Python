num = int(input("Digite o valor limite para gerar a série de Fibonacci: "))
n1 = 0
n2 = 1

fib = ''
if num == 1:
    fib = f"{n1}"
elif num == 2:
    fib = f"{n1} {n2}"
else:
    fib = f"{n1} {n2}"
    for i in range(num - 2):
        n = n1 + n2
        fib += f"{n} "
        n1 = n2
        n2 = n
print(f"A série de Fibonacci com {num} elementos é {fib}")