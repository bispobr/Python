x = int(input())
cont = 0
for c in range(x,x + 12):
    if c % 2 > 0:
        print(c)
        cont = cont + 1