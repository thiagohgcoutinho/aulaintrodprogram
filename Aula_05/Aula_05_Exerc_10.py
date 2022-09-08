t = str(" Aula 05 - Exercício 10 ")
print(f"{t:=^40}")
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
if n1<n2:
    print(f"O maior número é {n2}!")
elif n1>n2:
    print(f"O maior número é {n1}!")
else:
    print("Digite números diferentes!")