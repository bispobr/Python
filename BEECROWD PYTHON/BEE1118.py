notas_Validas = []
x = 0
while True:

    nota = float(input())
    if nota >= 0 and nota <=10:
        notas_Validas.append(nota)
    else:
        print("nota invalida")

    if len(notas_Validas) == 2:
        print(f"media = {sum(notas_Validas)/len(notas_Validas):.2f}")
        notas_Validas.clear()
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 1:
            continue
        while x != 2:
            print("novo calculo (1-sim 2-nao)")
            x = int(input())
            if x == 1:
                break

    if x == 1:
        continue
    elif x == 2 :
        break