while True:
    n = int(input())

    if n == 0:
        break

    for c in range(n):
        planeta, ano, distancia = [str(x)for x in input().split()]

        if c == 0:
            primerio = int(ano)-int(distancia)
            vencedor = planeta
        elif int(ano)-int(distancia) < primerio:
            primerio = int(ano)-int(distancia)
            vencedor = planeta
    print(vencedor)
