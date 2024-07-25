n= int(input().strip())
for c in range(n):
    t = int(input().strip())

    t = 2015 - t

    if(t <= 0):
        print(f'{1 - t} A.C.')
    else:
        print(f'{t} D.C.')