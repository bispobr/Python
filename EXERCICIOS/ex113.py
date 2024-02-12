def leiaint(msg):
    ok = False
    while not ok:
        try:
            n = int(input(msg))
            return n
            ok = True
        except:
            print('Erro! Digite um numero valido')


def leiafloat(msg):
    ok = False
    while not ok:
        try:
            n = float(input(msg))
            return n
            ok = True
        except:
            print('Erro! Digite um numero valido')


n= leiaint('Digite um numero Inteiro:')
c = leiafloat('Digite um numero Real:')
print(f'voce acabou de digitar o numero Inteiro :{n}')
print(f'voce acabou de digitar o numero Real :{c}')
