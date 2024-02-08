
def fatorial(a=0,show=False):
    if show == False:
        resultado = 1
        for n in range (1, a + 1):
            resultado *= n
        print(resultado)
    else:
        resultado = 1
        for n in range(1, a + 1):
            resultado *= n

        for c in range(5,0,-1):
            print(f'{c} x ', end="")
        print(resultado)


numero = int(input("Fatorial de: "))
fatorial(numero,True)