n = int(input())

for c in range(n):
    m = int(input())

    original = [int(x) for x in input().split(' ')]

    ordenado = sorted(original, reverse=True)

    resposta = 0
    for i in range(m):
        if(original[i] == ordenado[i]):
            resposta += 1

    print(resposta)
