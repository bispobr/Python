while True:
    n= int(input())
    if n==0:
        break
    amostra = [int(x) for x in str(input()).split(" ")]
    picos = 0
    for c in range(len(amostra)):
        anterior = amostra[((c - 1) + n) % n]
        proximo = amostra[(c + 1) % n]
        if (amostra[c]< anterior and amostra[c] < proximo) or  (amostra[c]> anterior and amostra[c] > proximo):
            picos +=1
    print(picos)