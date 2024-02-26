saque = int(input())
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
print(saque)
print('{} nota(s) de R$ 100,00'.format(qtd1))
print('{} nota(s) de R$ 50,00'.format(qtd2))
print('{} nota(s) de R$ 20,00'.format(qtd3))
print('{} nota(s) de R$ 10,00'.format(qtd4))
print('{} nota(s) de R$ 5,00'.format(qtd5))
print('{} nota(s) de R$ 2,00'.format(qtd6))
print('{} nota(s) de R$ 1,00'.format(qtd7))