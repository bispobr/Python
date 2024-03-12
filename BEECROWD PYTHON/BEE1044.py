valores = [int(x) for x in input().strip().split(' ')]
a = valores[0]
b = valores[1]
if(b > a):
    if(b % a == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if (a % b == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
