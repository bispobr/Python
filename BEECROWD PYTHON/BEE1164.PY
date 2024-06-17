n = int(input())
for c in range(n):
    soma = 0
    v = int(input())
    for d in range (1,v):
        if v % d == 0:
            soma+=d
    if soma == v:
        print(f'{v} eh perfeito')
    else:
        print(f"{v} nao eh perfeito")
        
    