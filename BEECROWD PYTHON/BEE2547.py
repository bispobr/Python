while(True):
    try:
        v = 0
        visitantes, Amin, Amax = [int (x) for x in input().split()]
        for c in range(visitantes):
            valor = int(input())
            if valor >= Amin and valor <= Amax:
                v +=1
        print(v)
            
    except EOFError:
        break