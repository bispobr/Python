import random
numero = list()
def sortear():

    for c in range (0,5):
        numero.append(random.randint(0,100))


def somapar():
    """
    trs
    """
    sp = 0
    for c in numero:
        if c % 2 == 0:
            sp+=c
    print(f'Soma Entre Todos os valores pares {sp}')

sortear()
print(numero)
somapar()


