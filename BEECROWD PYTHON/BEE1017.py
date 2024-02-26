tempo = int(input())
vel = int(input())
consumo = 12
distancia = tempo * vel
litros = distancia / consumo
print('{:.3f}'.format(litros))