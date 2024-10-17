while True:
    n = int(input())

    if n==0:
        break
    tempoTotal= 10
    tempoPessoas= [int (x) for x in input().split()]

    if n == 1:
        print(tempoTotal)
    else:
        for c in range(n - 1):
            tempoTotal+= min(10,tempoPessoas[c + 1]-tempoPessoas[c ] )
        print(tempoTotal)
        
