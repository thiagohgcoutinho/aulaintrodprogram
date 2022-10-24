import random

vetor = []

for i in range(30):
    t = random.randint(0, 30)
    vetor.append(t)

n = int(input("Digite o número que deseja pesquisar entre 0 e 30: "))

print(vetor)

if n in vetor:
    x = vetor.count(n)
    print(f"O número {n} apareceu {x} vezes na relação aleatória.")
else:
    print(f"O número {n} não apareceu na relação aleatória.")