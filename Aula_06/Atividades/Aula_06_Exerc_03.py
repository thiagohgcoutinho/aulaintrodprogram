t = str(" Aula 06 - Exercício 03 ")
print(f"{t:=^40}")
lista_amigos = ["Thiago", "Luiz", "Hugo", "Antônio"]

for x in lista_amigos:
    print(f"Boa aula, {x}!")

y = 0
while y < len(lista_amigos):
    print(f"Boa aula, {lista_amigos[y]}")
    y += 1