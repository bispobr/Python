jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador:'))
qtd = int(input("Quantidade de partidas jogada:"))
for c in range (0,qtd):
    partidas.append(int(input('Quantidade de Gol:')))
jogador['gols'] = partidas[:]
totalg = 0
for c in range (0,qtd):
    totalg += partidas[c]
jogador['totgols'] = totalg
print(jogador)

print('===' * 15)
for c,b in jogador.items():
    print(f'o Campo {c} tem valor {b}')

print("===" * 15)
print(f"O jogador {jogador['nome']} jogou {qtd} partidas")
for c in range (0,qtd):
    print(f'na partida{c}, fez {partidas[c]} gols')
print(f'foi um total de {jogador["totgols"]} gols')


