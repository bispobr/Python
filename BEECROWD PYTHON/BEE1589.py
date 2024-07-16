casos = int(input())

for c in range(casos):

    r1,r2 = [int (x) for x in str(input()).split()]
    print(f"{r1+r2}")