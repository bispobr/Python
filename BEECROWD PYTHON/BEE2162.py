medidas = int(input())
alturas = [int(x) for x in input().split()]

pico, vale, Padrao = False, False, True
for i in range(1, medidas):
    if (alturas[i] > alturas[i - 1] and not pico):
        pico = True
        vale = False
    elif (alturas[i] < alturas[i - 1] and not vale):
        pico = False
        vale = True
    else:
        Padrao = False
        break

print('1' if Padrao else '0')
