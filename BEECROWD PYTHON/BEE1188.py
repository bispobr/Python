m = [[0 for coluna in range(12)]for linha in range (12)]
soma = 0

op = str(input())

for linha in range (12):
    for coluna in range (12):
        valor = float(input())
        m[linha][coluna] = valor
        if  (linha > coluna) and (coluna + linha > 12-1) :
            soma+= valor
           

if op=="S":
    print ("{:.1f}".format(soma))
elif op == "M":
    print ("{:.1f}".format(soma/12))