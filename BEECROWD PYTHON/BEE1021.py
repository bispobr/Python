valor = str(input()).split('.')
saque = int(valor[0])
moeda = int(valor[1])
valor = saque
qtd1 = saque//100
resto = saque%100
qtd2 = resto//50
resto = resto % 50
qtd3 = resto//20
resto = resto %20
qtd4 = resto //10
resto = resto %10
qtd5 = resto //5
resto = resto %5
qtd6 = resto //2
resto = resto % 2
qtd7 = resto // 1
resto = resto % 1

qtd8 = moeda // 50
moeda = moeda % 50
qtd9 = moeda // 25
moeda = moeda % 25
qtd10 = moeda // 10
moeda = moeda % 10
qtd11 = moeda // 5
moeda = moeda % 5
qtd12 = moeda // 1

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(qtd1))
print('{} nota(s) de R$ 50.00'.format(qtd2))
print('{} nota(s) de R$ 20.00'.format(qtd3))
print('{} nota(s) de R$ 10.00'.format(qtd4))
print('{} nota(s) de R$ 5.00'.format(qtd5))
print('{} nota(s) de R$ 2.00'.format(qtd6))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(qtd7))
print('{} moeda(s) de R$ 0.50'.format(qtd8))
print('{} moeda(s) de R$ 0.25'.format(qtd9))
print('{} moeda(s) de R$ 0.10'.format(qtd10))
print('{} moeda(s) de R$ 0.05'.format(qtd11))
print('{} moeda(s) de R$ 0.01'.format(qtd12))