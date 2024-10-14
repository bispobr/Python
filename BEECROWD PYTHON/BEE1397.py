while True:
    n = int(input())

    if n == 0:
        break

    jogador1 = 0
    jogador2 = 0

    for c in range(n):
        a, b = [int(x)for x in input().split()]

        if a > b:
            jogador1 += 1
        elif b > a:
            jogador2 += 1

    print(f"{jogador1} {jogador2}")
