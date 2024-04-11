numero_casos_de_teste = int(input())
for c in range(numero_casos_de_teste):
    caso_de_teste = int(input())
    if caso_de_teste == 0:
        print("NULL")
    else:
        if caso_de_teste % 2 == 0:
            if caso_de_teste > 0:
                print("EVEN POSITIVE")
            elif caso_de_teste < 0:
                print("EVEN NEGATIVE")
        else:
            if caso_de_teste > 0:
                print("ODD POSITIVE")
            elif caso_de_teste < 0:
                print("ODD NEGATIVE")