n = int(input())
for c in range(n):
    palavra1= input()
    palavra2= input()
    palavra3= input()
    
    posicao3 = []

    for c in range (len(palavra3)):
        if palavra3[c] =="_":
            posicao3.append(c)

    if palavra1[posicao3[1]] == palavra2 [posicao3[0]]  or palavra1[posicao3[0]] == palavra2[posicao3[1]]:
        print("Y")
    else:        
        print("N")