while True:
    try:
        linha,coluna = [int (x) for x in input().split()]

        matriz = [[0 for _ in range(coluna + 2)] for _ in range(linha + 2)]


        for i in range(1, linha + 1):
            l = [int(x) for x in input().strip().split(' ')]
            for j in range(1, coluna + 1):
                matriz[i][j] = l[j - 1]

        for i in range(1, linha + 1):
            for j in range(1, coluna + 1):
                if(matriz[i][j] == 0):
                    print(matriz[i - 1][j] + matriz[i + 1][j] + matriz[i][j - 1] + matriz[i][j + 1], end='')
                else:
                    print(9, end='')
            print('')
    except EOFError:
        break