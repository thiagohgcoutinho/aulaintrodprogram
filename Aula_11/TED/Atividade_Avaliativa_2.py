#Questão 1
times = []

clube = str(input("Digite o nome do clube para adicionar a lista: ")).lower()
times.append(clube)

while len(times) <= 10:
    clube = str(input("Digite o nome do próximo clube: ")).lower()
    if clube in times:
        print("--- Clube já adicionado!! ---")
    else:
        times.append(clube)
    
print("---"*5, "Número de clubes máximo atingido!", "---"*5)

pesq = str(input("Digite o nome do clube que deseja pesquisar: ")).lower()

if pesq in times:
    print(f"Encontrei o clube {pesq.title()} na lista.")
else:
    print(f"Não encontrei o clube {pesq.title()} na lista.")


#Questão 2
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