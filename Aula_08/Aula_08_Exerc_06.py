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