def aumentar (a,taxa,f='s'):
    if f == 's':
        valor = a + (a*taxa)/(100)
        return moeda(valor)
    else:
        valor = a + (a * taxa) / (100)
        return valor


def diminuir (b,taxa,f='s'):
    if f =='s':
        valor2 = b - (b *taxa)/(100)
        return moeda(valor2)
    else:
        valor2 = b - (b * taxa) / (100)
        return valor2


def dobro(c,f='s'):
    if f=='s':
        valor3 = c * 2
        return moeda(valor3)
    else:
        valor3 = c * 2
        return valor3


def metade (d, f='s'):
    if f=='s':
        valor4 = d /2
        return moeda(valor4)
    else:
        valor4 = d / 2
        return valor4

def moeda(preco=0,moeda = 'R$' ):
    return f'{moeda}{preco:.2f}'.replace('.',',')