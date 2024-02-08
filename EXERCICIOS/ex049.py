num = int(input("tabuada de:"))
fim = int(input("ate:"))
for c in range(0, fim + 1):
    m = num * c
    print("{} x {}: {}".format(num,c,m))