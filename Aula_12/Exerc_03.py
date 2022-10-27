vetor = [
    10, 20, 30,
    50, 60, 70,
    3, 6, 7, 91
]

#print(max(vetor))
#print(min(vetor))

n = vetor[0]
x = vetor[0]

for q in vetor:
    if q > n:
        n = q
    if q < x:
        x = q

print(f"O maior valor é {n} e seu índice é {vetor.index(n)}")
print(f"O menor valor é {x} e sei índice é {vetor.index(x)}")

