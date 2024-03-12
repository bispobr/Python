valores = [int(x) for x in input().strip().split(' ')]
inicio = valores[0]
fim = valores[1]
if fim <= inicio:
    jogo = fim + 24 - inicio
else:
    jogo = fim - inicio

print("O JOGO DUROU {} HORA(S)".format(jogo))