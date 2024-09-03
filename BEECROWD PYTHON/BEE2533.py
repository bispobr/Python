while True:
    
    try:
        m = int(input())
        numerador, denominador = 0, 0
        for c in range(m):
            nota, carga = [int (x) for x in input().split()]
            numerador += nota * carga
            denominador += carga

        print(f'{(numerador/(100 * denominador)):.4f}')
    
    except EOFError:
        break