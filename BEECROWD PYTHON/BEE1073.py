valor = int(input())
for c in range(1,valor + 1):
    if c % 2 == 0:
        print("{}^2 = {}".format(c,pow(c,2)))