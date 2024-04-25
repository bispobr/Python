x = int(input())
y = int(input())

if x > y:
    aux = y
    y = x
    x = aux

soma = 0
for c in range(x,y+1):
    if (c % 13 != 0):
        soma +=c

print(soma)


