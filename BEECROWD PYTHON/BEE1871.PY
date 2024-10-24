while True:
    try:
        m, n = [int(x) for x in input().strip().split(' ')]

        if( m and  n == 0):
            break

        soma = str(m + n)
       
        print(soma.replace('0', ""))
    except EOFError:
        break