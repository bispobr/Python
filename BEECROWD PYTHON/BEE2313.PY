lado = [int (x) for x in input().split()]
lado.sort()

if (lado[0] < lado[1] + lado[2] and lado[1] < lado[0] + lado[2] and lado[2] < lado[0] + lado[1] ):
    print("Valido-", end="")
    if (lado[0] == lado[1] == lado[2]):
        print("Equilatero")
    elif (lado[0] == lado[1] or lado[0] == lado[2] or lado[1] == lado[2]):
        print("Isoceles")
    else:
        print("Escaleno")

    if (lado[0] % 3 == 0 and lado[1] % 4 == 0 and lado[2] % 5 == 0):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")