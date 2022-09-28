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