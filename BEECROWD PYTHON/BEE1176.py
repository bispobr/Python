fib = []
caso = int(input())

for c in range(caso):
    n = int(input())
    ultimo=1
    penultimo=1

    if (n== 0):
        fib.append(0)

    if (n==1) or (n==2):
        fib.append(1)
    elif (n > 0):
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
        fib.append(termo)

    print("Fib({}) = {}".format(n,fib[c]))
    
