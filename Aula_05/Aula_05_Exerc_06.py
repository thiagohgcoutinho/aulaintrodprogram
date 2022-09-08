t = str(" Aula 05 - Exercício 06 ")
print(f"{t:=^40}")
n = float(input("Digite um número: "))
if n<10:
    print(f"O número {n} é menor que 10!")
elif n>10:
    print(f"o número {n} é maior que 10!")
else:
    print("Você digitou o número 10!")