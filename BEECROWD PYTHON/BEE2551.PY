while True:
    try:
        diasTreino = int(input())
        mediaRecord = 0
        mediatreino = 0
        for c in range(diasTreino):
            tempo, distancia = [int (x) for x in input().split()]
            mediatreino = distancia / tempo

            if mediatreino > mediaRecord:
                mediaRecord = mediatreino
                print(c + 1)

    except EOFError:
        break