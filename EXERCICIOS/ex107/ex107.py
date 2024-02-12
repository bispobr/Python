import moeda
num = int(input('digite um valor:'))
print(f' o dobro de R${num} é {moeda.dobro(num)}')
print(f' a metade de R${num} é {moeda.metade(num)}')
print(f' Aumento de 10%, trmos R${moeda.aumentar(num,10)}')
print(f' Diminuição de 10%, trmos R${moeda.diminuir(num,10)}')


