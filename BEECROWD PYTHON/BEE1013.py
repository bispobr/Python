def maior (a,b):
    m = (a + b + abs(a - b)) / 2
    return m

valores = str(input()).split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
maio = maior(a,maior(b,c))

print('{:.0f} eh o maior'.format(maio))