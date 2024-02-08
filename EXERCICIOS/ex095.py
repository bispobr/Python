jogador = dict()
partidas = list()
jogadores = list()
while True:
    jogador['nome'] = str(input('Nome do jogador:'))
    qtd = int(input("Quantidade de partidas jogada:"))
    partidas.clear()
    for c in range (0,qtd):
        partidas.append(int(input('Quantidade de Gol:')))
    jogador['gols'] = partidas[:]
    totalg = 0
    for c in range (0,qtd):
        totalg += partidas[c]
    jogador['totgols'] = totalg
    jogadores.append(jogador.copy())
    print(jogadores)
    jogador.clear()
    resp = str(input("Quer continuar? [S/N}")).upper()
    if resp == "N":
        break
print('***'*15)
for a in range (0,len(jogadores)):
    print(f'Cod {a} nome {jogadores[a]["nome"]} gols {jogadores[a]["gols"]} Total {jogadores[a]["totgols"]}')
print('***' * 15)
while True:
    cod = int(input("Mostrat dados de qual jogador? (999 para parar)"))
    if cod == 999:
        break
    print(f'Levantamento do jogador {jogadores[cod]["nome"]} ')
    for i,g in enumerate(jogadores[cod]['gols']):
        print(f'no jogo {i + 1} fez {g}')
    print('***' * 15)








