n = int (input())

for c in range(n):
    inicio, fim= [int(x)for x in input().split()]

    sequencia = ""

    for c in range(inicio,fim + 1):
        sequencia += str(c) 
        

    sequencia += sequencia[::-1]

    print(sequencia)