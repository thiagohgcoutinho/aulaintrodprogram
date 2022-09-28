t = str(" Aula 08 - Exercício 01 ")
print(f"{t:=^40}")
print("Cálculo da raíz do segundo grau")
print("Ax^2 + Bx + C")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = (b * b) - 4 * a * c
print(f"O valor de delta é: {delta}")
if delta > 0:
    x1 = ((-b) + (delta)**(1/2)) / (2 * a)
    x2 = ((-b) - (delta)**(1/2)) / (2 * a)
    print(f"As raís da equação são x1 = {x1} e x2 = {x2}")
elif delta == 0:
    x = (-1 * b) / (2 * a)
    print(f"O valor das raízes x1 e x2 é {x}")
else: 
    print("A equação não possui raízes reais.")

#import math

#a = float(input("Digite o valor A: "))
#b = float(input("Digite o valor B: "))
#c = float(input("Digite o valor C: "))

#delta = math.pow(b, 2) - 4 * a * c
#if delta > 0:
#    x1 = (-b + math.sqrt(delta)) / (2 * a)
#    x2 = (-b - math.sqrt(delta)) / (2 * a)

#    print(f"X1 -> {x1:.2f}")
#    print(f"X2 -> {x2:.2f}")
#    print(f"Delta -> {delta}")
#else:
#    print("Reduza os valores de A e C!")
