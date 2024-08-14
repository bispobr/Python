while True:
    try:
        sair = False
        casos = int(input())

        for c in range(casos):
            pessoas = int(input())

            if pessoas == 0:
                sair= True
                break

            if pessoas % 2 == 0:
                print((pessoas * 2) - 2)
            else:
                print((pessoas * 2) - 1)

        if sair :
            break
    except EOFError:
        break