from utilidadescev import moeda
num = int(input('digite um valor:'))
print(f' o dobro de {moeda.moeda(num)} é {moeda.dobro(num,'s')}')
print(f' a metade de {moeda.moeda(num)} é {(moeda.metade(num))}')
print(f' Aumento de 10%, temos {moeda.aumentar(num,15) }')
print(f' Diminuição de 10%, temos {moeda.diminuir(num,10)}')


print()


