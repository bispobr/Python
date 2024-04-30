x,y = [int(x) for x in str(input()).split()]

inicio = 1
for d in range(0,y+1):
    for c in range (inicio, inicio + x):
        if c== y +1:
            break
        print(c,end=" ")
    print()
    if c == y +1:
        break
    inicio+=x