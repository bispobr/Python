def divisao (x,y):
    if y == 0:
        resultado = f"divisao impossivel"
    else:
        resultado = f"{x / y :.1f}"
    return resultado

qts_casos = int(input())
for c in range(qts_casos):
    x,y = [int (x) for x in str(input()).split()]
    print(divisao(x,y))

