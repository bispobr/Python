def menor_maior(m,n):
    if m > n:
        [m,n] = [n,m]
    return n,m

while True:
    soma = 0
    m,n = [int (x) for x in str(input()).split()]
    if m <= 0 or n <=0:
        break
    n,m = menor_maior(m,n)
    for c in range (m,n +1,1):
        print(c,end=" ")
        soma += c
    print(f'Sum={soma}')

