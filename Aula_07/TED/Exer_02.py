t = str(" Aula 07 - Exercício 02 - TED ")
print(f"{t:=^40}")
nasc = int(input("Qual ano você nasceu? "))
atual = int(input("Qual o ano atual? "))
idade = atual - nasc
if idade < 16:
    print(f"Como você tem {idade} anos, você ainda não pode votar.")
elif 16 <= idade < 18:
    print(f"Como você tem {idade} anos, você já pode votar.")
else:
    print(f"Como você tem {idade} anos, você já deve votar.")