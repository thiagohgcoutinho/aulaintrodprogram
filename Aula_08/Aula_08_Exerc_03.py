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