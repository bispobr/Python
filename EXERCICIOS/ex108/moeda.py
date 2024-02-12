def aumentar (a,taxa):
    valor = a + (a*taxa)/(100)
    return valor


def diminuir (b,taxa):
    valor2 = b - (b *taxa)/(100)
    return valor2


def dobro(c):
    valor3 = c * 2
    return valor3


def metade (d):
    valor4 = d /2
    return valor4


def moeda(preco=0,moeda = 'R$' ):
    return f'{moeda}{preco:.2f}'.replace('.',',')