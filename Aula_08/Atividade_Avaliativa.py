#Atividade Avaliativa
# Questão 1
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

# Questão 2
from math import pow , sqrt
t = str(" Aula 08 - Exercício 02 ")
print(f"{t:=^40}")
px = float(input("Digite o valor de x do ponto P: "))
py = float(input("Digite o valor de y do ponto P: "))
qx = float(input("Digite o valor de x do ponto Q: "))
qy = float(input("Digite o valor de y do ponto Q: "))
d = sqrt(pow((qx - px),2) + pow((qy - py),2))
print(f"A distância entre os pontos P e Q é {d:.2f}")

# Questão 3
t = str(" Aula 08 - Exercício 03 ")
print(f"{t:=^40}")
print("CALCULADORA")
print("Escolha dois números e a opração entre eles.")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Digite 1 para ADIÇÃO")
print("Digite 2 para SUBTRAÇÃO")
print("Digite 3 para MULTIPLICAÇÃO")
print("Digite 4 para DIVISÃO")
print("Digite 5 para POTENCIAÇÃO")
operacao = int(input("Qual operação matemática: "))

if operacao == 1:
    print(f"A soma de {n1} com {n2} é {n1 + n2}!")
elif operacao == 2:
    print(f"A subtração entre {n1} e {n2} é {n1 - n2}!")
elif operacao == 3:
    print(f"A multiplicação de {n1} por {n2} é {n1 * n2}!")
elif operacao == 4:
    print(f"A divisão de {n1} e {n2} é {n1 / n2}!")
elif operacao == 5:
    print(f"A potência de {n1} por {n2} é {n1 ** n2}!")
else:
    print("Escolha uma operação válida!")

# Questão 4
t = str(" Aula 08 - Exercício 04 ")
print(f"{t:=^40}")
massa = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = massa / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC foi {imc}")
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC foi {imc}")
    print("Você está no peso ideal. Parabéns!")
elif 25 <= imc < 30:
    print(f"Seu IMC foi {imc}")
    print("Você está acima do peso.")
else:
    print(f"Seu IMC foi {imc}")
    print("Você está na obesidade.")

# Questão 05
t = str(" Aula 08 - Exercício 05 ")
print(f"{t:=^40}")
print("")
grupo1 = []
grupo2 = []
grupo3 = []
grupo4 = []
num = 100
while num >= 0:
    print("Digite um número negativo para encerrar!")
    num = float(input("Digite um número para a lista entre 0 e 100: "))
    if 0 <= num <= 100:
        if 0 <= num <= 25:
            grupo1.append(num)
        elif 26 <= num <= 50:
            grupo2.append(num)
        elif 51 <= num <= 75:
            grupo3.append(num)
        else:
            grupo4.append(num)
    elif num > 100:
        print("Número acima de 100 não é permitido!")
    else:
        print("Lista encerrada.")

print(f"A quantidade de número entre 0 e 25 foi {len(grupo1)}!")
print(f"A quantidade de número entre 26 e 50 foi {len(grupo2)}!")
print(f"A quantidade de número entre 51 e 75 foi {len(grupo3)}!")
print(f"A quantidade de número entre 76 e 100 foi {len(grupo4)}!")

# Questão 6
t = str(" Aula 08 - Exercício 06 ")
print(f"{t:=^40}")
print(" ")
print("FATORIAL DE UM NÚMERO")
print(" ")
n = int(input("Digite o número: "))
res = 1
for i in range(1, n+1):
    res *= i
print(f"O resultado de {n}! é {res}.")