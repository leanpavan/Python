c = float(input("asda"))
i = float(input("asda"))
n = int(input("asda"))
m = 0
for _ in range(n):
    m += c * (1 + i) ** n
    print(f"{m:.2f}")