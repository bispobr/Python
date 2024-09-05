while True:
    try:
        cartasM = []
        cartasL = []
        atributos = int(input())
        [qtdcartasM,qtdcartasL] = [int (x) for x in input().split()]

        for c in range(qtdcartasM):
            cartas = [int (x) for x in input().split()]
            cartasM.append(cartas.copy())

        for c in range(qtdcartasL):
            cartas = [int (x) for x in input().split()]
            cartasL.append(cartas.copy())

        [escolhaM,escolhaL] = [int (x) for x in input().split()]

        atributo = int(input())

        if cartasM[escolhaM -1] [atributo - 1] > cartasL[escolhaL -1] [atributo - 1]:
            print("Marcos")
        elif cartasL[escolhaL -1] [atributo - 1] > cartasM[escolhaM -1] [atributo - 1] :
            print("Leonardo")
        else:
            print("Empate")


    except EOFError:
        break