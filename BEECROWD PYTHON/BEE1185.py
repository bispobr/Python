m = [[0 for coluna in range (12)] for linha in range (12)]
soma = 0
cont = 0

op = str(input())

for linha in range(12):
    for coluna in range (12):
        valor = float(input())
        m[linha] [coluna] = valor
        if  coluna + linha < 12 - 1 :
            soma+=valor
            cont+=1

if op == "S":
    print("{:.1f}".format(soma))
elif op == "M":
    print("{:.1f}".format(soma/cont))