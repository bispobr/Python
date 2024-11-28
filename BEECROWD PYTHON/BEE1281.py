n = int(input())

for _ in range(n):
    m = int(input())

    precos = {}

    for c in range(m):
        fruta, preco = input().strip().split(' ')

        precos[fruta] = float(preco)

    p = int(input())

    resposta = 0.0
    for d in range(p):
        fruta, quantidade = input().strip().split(' ')

        resposta += int(quantidade) * precos[fruta]

    print(f'R$ {resposta:.2f}')