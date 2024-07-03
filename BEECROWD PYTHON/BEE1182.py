m = [ [0 for i in range(12)] for j in range(12)]
soma = 0

coluna = int(input())
operacao = str(input())


for linha in range (12):
    for c in range (12):
        valor = float(input())
        m[linha][c] = valor
        if c == coluna:
            soma += valor        

if operacao == "S":
    print("{:.1f}".format(soma))
elif operacao == "M":
    print("{:.1f}".format(soma/12))


