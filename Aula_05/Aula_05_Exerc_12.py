t = str(" Aula 05 - Exercício 12 ")
print(f"{t:=^40}")
c = int(input("Digite sua conta sem o dígito: "))
s = float(input("Digite o saldo atual da sua conta: "))
d = float(input("Digite os débitos: "))
cr = float(input("Digite os créditos: "))
sa = s - d + cr
if sa>=0:
    print(f"Saldo POSITIVO de R$ {sa:.2f}!")
else:
    print(f"Saldo NEGATIVO de R$ {sa:.2f}!")