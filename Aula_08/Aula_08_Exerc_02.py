from math import pow , sqrt
t = str(" Aula 08 - Exercício 02 ")
print(f"{t:=^40}")
px = float(input("Digite o valor de x do ponto P: "))
py = float(input("Digite o valor de y do ponto P: "))
qx = float(input("Digite o valor de x do ponto Q: "))
qy = float(input("Digite o valor de y do ponto Q: "))
d = sqrt(pow((qx - px),2) + pow((qy - py),2))
print(f"A distância entre os pontos P e Q é {d:.2f}")