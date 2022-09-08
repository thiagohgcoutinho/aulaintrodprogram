t = str(" Aula 05 - Exercício 09 ")
print(f"{t:=^40}")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
if m>=6:
    print(f"A média do aluno é {m:.1f}, sendo assim, APROVADO!")
else:
    print(f"A média do aluno é {m:.1f}, sendo assim, REPROVADO!")