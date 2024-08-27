while (True):
    try:
        n ,identificacao = [int (x) for x in input().split()]

        cs = 0
        for c in range (n):
            id ,jogo = [int (x) for x in input().split()]

            if id == identificacao and jogo == 0:
                cs+=1

        print(cs)
    except EOFError:
        break