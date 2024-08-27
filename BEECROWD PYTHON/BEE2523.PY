while (True):
    try:
        alfabeto = str(input())
        lampadas = int(input())
        piscadas = [int (x) for x in input().split()]
        for c in range(lampadas):
            print(alfabeto[piscadas[c]-1], end = "")
        print()

    except EOFError:
        break;