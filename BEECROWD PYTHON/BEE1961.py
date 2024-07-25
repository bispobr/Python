p,n = [int (x) for x in input().strip().split(' ')]
canos = [int (x) for x in input().strip().split(' ')]

for c in range(n-1):
    if canos[c] > canos[c +1]:
        if p >= (canos[c] - canos[c +1]):
            resultado = "YOU WIN"
        else:
            resultado = "GAME OVER"
            break
            
    else:
         if p >= ( canos[c +1] - canos[c]):
            resultado = "YOU WIN"
         else:
            resultado = "GAME OVER"
            break

print(f'{resultado}')            


