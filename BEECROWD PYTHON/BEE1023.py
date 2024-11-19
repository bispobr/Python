import math

#Otimizar Time limit exceeded

t = 0
while True:
    try:
        n = int(input())

        if(n == 0):
            break

        if(t):
            print('')

        totalX, totalY = 0, 0
        consumos = {}
        for c in range(n):
            X, Y = [int (x) for x in input().split(" ")]

            totalX += X
            totalY += Y

            if (Y//X in consumos):
                consumos[Y//X] += X
            else:
                consumos[Y//X] = X

        consumo_total = ((100 * totalY)/totalX)/100

        t += 1
        print(f'Cidade# {t}:')

        output = []
        keys = sorted(list(consumos.keys()))
        for key in keys:
            output.append(f'{consumos[key]}-{key}')

        print(f'{" ".join(output)}')

        consumo_medio = math.floor((100 * totalY)/totalX)/100

        print(f'Consumo medio: {consumo_medio:.2f} m3.')
    except EOFError:
        break