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
    num = float(input("Digite um número para a sua lista entre 0 e 100: "))
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