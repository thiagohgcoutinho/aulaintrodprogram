t = str(" Aula 07 - Exercício 01 - TED ")
print(f"{t:=^40}")
m = int(input("Quantas maçãs deseja comprar? "))
if m<12:
    v = 1.30
    print(f"O valor total para {m} maçãs será R$ {m * v:.2f}!")
else:
    v = 1.00
    print(f"O valor total para {m} maçãs será R$ {m * v:.2f}!")