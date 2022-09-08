t = str(" Aula 05 - Exercício 13 ")
print(f"{t:=^40}")
qmax = int(input("Qual a quantidade máxima de estoque do produto? "))
qmin = int(input("Qual a quantidade mínima de estoque do produto? "))
qmed = (qmax + qmin)/2
qatual = int(input("Qual a quantidade atual de produtos? "))
if qatual>=qmed:
    print(f"A quantidade média do produto em estoque é de {qmed:.0f}, e a quantidade atual é {qatual}, assim, NÃO EFETUAR COMPRA!")
else:
    print(f"A quantidade média do produto em estoque é de {qmed:.0f}, e a quantidade atual é {qatual}, assim, EFETUAR COMPRA!")