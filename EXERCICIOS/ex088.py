from random import randint
lista = list ()
jogo = list ()
qtdjogos = int(input('Quantos jogos voce quer que eu sorteie?: '))
for c in range(0,qtdjogos):
    for d in range (0,6):
        lista.append(randint(0, 60))
    jogo.append(lista[:])
    lista.clear()
for e in range(0,qtdjogos):
    print(f'Jogo {e + 1} : {sorted(jogo[e])}')


