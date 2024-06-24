
n = int(input())
valores = [int (x) for x in str(input()).split()]
print("Menor valor: {}".format(min(valores)))
print("Posicao: {}".format(valores.index(min(valores))))
