from random import randint

a = []
b = []
n = []

for i in range(10):
    a.append(randint(0, 10))

for i in range(10):
    b.append(randint(0, 10))
    
for i in range(10):
    n.append(a[i] + b[i])

print(a)
print(b)
print(n)