while(True):
    try:
        n = int(input())

        m = [[0 for c in range(n)] for l in range(n)]

        for linha in range(n):
            for coluna in range (n):
                if linha + coluna == n-1:
                    m[linha][coluna] = 2
                elif linha == coluna:
                    m[linha][coluna] = 1
                else: 
                    m[linha][coluna] = 3

        for linha in range(n):
           for coluna in range (n):
                print(m[linha][coluna], end='')
           print('')   

       
    except EOFError:
        break