m = [ [0 for i in range(12)] for j in range(12)]
soma = 0

linha = int(input())
operacao = str(input())


for l in range (12):
    for coluna in range (12):
        valor = float(input())
        m[l][coluna] = valor
        if l == linha:
            soma += valor        

if operacao == "S":
    print("{:.1f}".format(soma))
elif operacao == "M":
    print("{:.1f}".format(soma/12))


