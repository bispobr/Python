n = int(input())

pares=[]
impares=[]

for c in range (n):
    valor = int(input())

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort(reverse=True)

for p in pares:
    print(p)
for i in impares:
    print(i)

