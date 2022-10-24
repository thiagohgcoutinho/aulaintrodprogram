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
    print(f"ACHEI. Encontrei o clube {pesq.title()} na lista.")
else:
    print(f"NÃO ACHEI. Não encontrei o clube {pesq.title()} na lista.")