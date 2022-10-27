notas = []
x = 0
c = 0

for i in range(20):
    n = float(input("Digite a nota do aluno: "))
    notas.append(n)

for n in notas:
    x = x + n

#poderia usar a função de soma -> soma = sum(notas)

media = x / len(notas)

for np in notas:
    if np > media:
        c = c + 1

print(f"A média da turma foi {(media):.1f} e tiveram {c} alunos com nota acima da média.")