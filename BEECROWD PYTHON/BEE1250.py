n = int(input())
for c in range(n):
    t= int(input())
    tiros = [int(x) for x in str(input()).split()]
    pulos = str(input())
    atingido = 0
    for d in range(t):
        if (pulos[d] == "S" and tiros[d] < 3) or (pulos[d] == "J" and tiros[d] > 2):
            atingido+=1
    print(atingido)

