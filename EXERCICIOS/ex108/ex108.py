import moeda
num = int(input('digite um valor:'))
print(f' o dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f' a metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f' Aumento de 10%, temos {moeda.moeda(moeda.aumentar(num,10)) }')
print(f' Diminuição de 10%, temos {moeda.moeda(moeda.diminuir(num,10))}')


