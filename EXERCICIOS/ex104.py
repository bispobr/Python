def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Errp! Digite um numero valido')
        if ok:
            break
    return valor


n= leiaint('Digite um numero')
print(f'voce acabou de digitar o numero {n}')