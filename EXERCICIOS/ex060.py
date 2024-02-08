n=int(input("digite um numero para calcular o fatorial:"))
c=n
m=1
while c>0:
    m*=c
    c-=1
print("O fatorial de {} é :{}".format(n,m))