while True:
    n = int(input())

    if n ==0:
        break;

    m = [ [ 0 for coluna in range (n) ] for linha in range (n)]

    for linha in range (n):
        for coluna in range (n):

                m[linha][coluna] = (min(min(linha, n - linha - 1), min(coluna, n - coluna - 1)) + 1)

    for linha in range (n):
        for coluna in range (n):
            print(f'{m[linha][coluna]:3d}',end='')
        print('')
    print('')