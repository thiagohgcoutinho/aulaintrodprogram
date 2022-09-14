""" Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 e que,
quando dividido por 11, produzam resto igual a 5."""

t = str(" Aula 06 - Exercício 01 ")
print(f"{t:=^40}")
for x in range(1000, 2001):
    if ( x % 11 ) == 5:
        print(x)