t = str(" Aula 05 - Exercício 11 ")
print(f"{t:=^40}")
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
if n1<n2:
    print(f"A sequência do menor para o maior é {n1} e {n2}!")
elif n1>n2:
    print(f"A sequência do menor para o maior é {n2} e {n1}!")
else:
    print("Digite números diferentes!")