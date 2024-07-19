import math

t = int(input())
for c in range(t):
    pa, pb, g1, g2 = input().strip().split(' ')
    pa, pb = int(pa), int(pb)
    g1, g2 = float(g1)/100, float(g2)/100

    anos = 1
    while(pa <= pb and anos < 101):
        pa += math.floor(pa * g1)
        pb += math.floor(pb * g2)
        anos += 1

    if(pa <= pb):
        print('Mais de 1 seculo.')
    else:
        print(f'{anos - 1} anos.')