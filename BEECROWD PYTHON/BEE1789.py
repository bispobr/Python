while(True):
    try:
        casos = int(input())
        velocidades = [int (x) for x in str(input()).split()]

        maior = max(velocidades)

        if maior >= 20:
            print(3)
        elif maior >= 10:
            print(2)
        else:
            print(1)
    except EOFError:
        break