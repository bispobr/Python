def ficha(nome='<Desconhecido>',gols=0):
    print(f'o jogador {nome} fem {gols} gol(s) ')

jogador = str(input('Nome do Jogador:'))
nume = str(input('numero de Gols:'))
if nume.isnumeric():
    num = int(nume)
else:
    num = 0

ficha(jogador,nume)