while(True):
    try:
        lista = []
        habitantes, consultas = [int (x) for x in input().split()]
        for c in range(habitantes):
            valor = int(input())
            lista.append(valor)

        lista.sort(reverse=True)

        for d in range(consultas):
            indice = int(input())
            print(lista[indice - 1])
    except EOFError:
        break