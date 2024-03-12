valores = [int(x) for x in input().strip().split(' ')]
hinicio = valores[0]
minicio = valores[1]
hfinal = valores[2]
mfinal = valores[3]

minicio += hinicio*60
mfinal += hfinal*60

duracao = mfinal - minicio;

if duracao <= 0:
    duracao+= 24*60

horas = duracao//60
minutos = duracao % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas,minutos))