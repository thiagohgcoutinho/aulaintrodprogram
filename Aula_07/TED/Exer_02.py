t = str(" Aula 07 - Exercício 02 - TED ")
print(f"{t:=^40}")
nasc = int(input("Qual ano você nasceu? "))
atual = int(input("Qual o ano atual? "))
if (atual - nasc) < 16:
    print(f"Como você tem {(atual - nasc)} anos, você ainda não pode votar.")
elif 16 <= (atual - nasc) < 18:
    print(f"Como você tem {(atual - nasc)} anos, você já pode votar.")
else:
    print(f"Como você tem {(atual - nasc)} anos, você já deve votar.")