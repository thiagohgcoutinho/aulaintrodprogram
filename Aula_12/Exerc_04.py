from random import randint

lista = []
nova_lista = []

for i in range(10):
    lista.append(randint(0,100))

x = randint(1,9)

for i in range(len(lista)):
    nova_lista.append(x * lista[i])
    
print(lista)
print(x)
print(nova_lista)