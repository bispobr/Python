qtd_Casos = int(input())
for c in range(qtd_Casos):
    x,y = [int (x) for x in str(input()).split()]
    soma = 0
    if x==y:
        print(0)
    elif (x < y):
        for c in range(x + 1,y,1):
            if c%2 !=0:
               soma+=c
        print(soma)
    elif (y < x):
        for c in range(y +1,x,1):
            if c%2 !=0:
               soma+=c
        print(soma)