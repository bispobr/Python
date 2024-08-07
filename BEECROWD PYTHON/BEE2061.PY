n ,m = [int (x) for x in input().split()]

for c in range (m):
    frase = str(input())

    if frase == "fechou":
        n+=1
    elif frase == "clicou":
        n-=1

print(n)
