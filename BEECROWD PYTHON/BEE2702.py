refeicao = [int (x) for x in input().split()]
pedidos = [int (x) for x in input().split()]

res = 0

for c in range(3):
    if pedidos[c] > refeicao[c]:
        res += pedidos[c] - refeicao[c]

print(res)