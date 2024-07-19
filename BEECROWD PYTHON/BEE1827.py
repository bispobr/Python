while(True):
    try:
        n = int(input())

        m = [[0 for c in range(n)] for l in range(n)]

        for linha in range(n):
            for coluna in range (n):
                

                if (linha == n // 2 and coluna == n // 2):
                    m[linha][coluna] = 4
                elif (n // 3 <= linha < n - n // 3 and n // 3 <= coluna < n - n // 3):
                    m[linha][coluna] = 1
                elif (linha == coluna):
                    m[linha][coluna] = 2
                elif (linha + coluna == n - 1 ):
                    m[linha][coluna] = 3
                else:
                    m[linha][coluna] = 0

        for linha in range(n):
           for coluna in range (n):
                print(m[linha][coluna], end='')
           print('')
        print('')   

       
    except EOFError:
        break