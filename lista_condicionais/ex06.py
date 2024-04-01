'''
6. Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
raízes devem ser calculadas pela fórmula de Bhaskara, como segue:
'''
import math

a, b, c = map(int,input("Fornecer os valores dos coeficientes A, B e C para o cálculo da equação de segundo grau: ").split())

# Calcular o delta
discriminante = (b**2) - (4 * a * c)

if discriminante < 0:
    print(f"Não existe raízes reais para o delta {discriminante:.2f}")
else:
    raiz_delta = math.sqrt(abs(discriminante))

    # Calcular duas soluções pra raíz
    sol1 = (-b + raiz_delta) / (2 * a)
    sol2 = (-b - raiz_delta) / (2 * a)

print(f"As soluções para a equação de segundo grau fornecida são {sol1} e {sol2}")



