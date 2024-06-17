caso_de_teste = int (input())
for c in range(caso_de_teste):
    valor = int(input())
    cont = 0
    for d in range(1,valor+1):
        if valor % d == 0:
            cont +=1
    if cont == 2:
        print(f"{valor} eh primo")
    else:
        print(f"{valor} nao eh primo")