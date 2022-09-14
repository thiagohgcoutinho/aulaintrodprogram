"""Faça um programa que mostre as tabuadas de 1 a 10"""

t = str(" Aula 06 - Exercício 02 ")
print(f"{t:=^40}")
for x in range(1, 11):
    print(f"Tabuada do {x}!")
    for y in range(1, 11):
        z = x * y
        print(f"{x} x {y} = {z}")