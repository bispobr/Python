from random import randint
jogo = {'jogador1': randint(1,10),
        'jogador2': randint(1,10),
        'jogador3': randint(1,10),
        'jogador4': randint(1,10),

}

for a,b in jogo.items():
    print(f'{a} tirou o dado {b}')
print('++'*15)
print('rankng dos Jogadores')
for c in sorted(jogo,key=jogo.get,reverse=True):
    print(c)


