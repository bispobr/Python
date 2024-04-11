casos_de_teste = int(input())
for c in range (casos_de_teste):
    v1,v2,v3 = [float (x) for x in str(input()).split()]
    media = ((v1 * 2) + (v2 * 3) + (v3 *5)) / 10
    print('{:.1f}'.format(media))