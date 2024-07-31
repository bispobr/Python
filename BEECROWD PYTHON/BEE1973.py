estrelas = int(input())
fazendas = [int (x) for x in input().strip().split(' ')]

c = 0
visita = 0
while c >=0 and c <estrelas:
    
    if c > visita: visita =c

    if fazendas[c] % 2 == 1:
        if fazendas[c] != 0:fazendas[c]-=1
        c+=1  
    elif fazendas[c] % 2 == 0:
       if fazendas[c] != 0:fazendas[c]-=1
       c-=1
       
print(f"{visita + 1} {sum(fazendas)}")