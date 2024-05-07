def delta(a, b, c):
    return b**2 -4*a*c


def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("As raízes são imaginárias")
        return 0, 0, False

    x1 = (-b + d**(1/2))/2 * a
    x2 = (-b - d **(1 / 2))/2 * a
    return x1, x2


a = int(input("Digite o A: "))
b = int(input("Digite o B: "))
c = int(input("Digite o C: "))
raiz1 = bhaskara(a,b,c)
print(raiz1)