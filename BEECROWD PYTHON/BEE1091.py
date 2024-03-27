while True:
    k = int(input())
    if k ==0: break
    pontoDivisor = [int(x) for x in str(input()).split()]
    for c in range(k):
        residencia = [int(x) for x in str(input()).split()]

        if residencia[0] > pontoDivisor[0]:
            if residencia[1] > pontoDivisor[1]:
                print("NE")
            elif residencia[1] < pontoDivisor[1]:
                print("SE")
            else:
                print("divisa")
        elif residencia[0] < pontoDivisor[0]:
            if residencia[1] > pontoDivisor[1]:
                print("NO")
            elif residencia[1] < pontoDivisor[1]:
                print("SO")
            else:
                print("divisa")
        else:
            if residencia[1] > pontoDivisor[1]:
                print("divisa")
            elif residencia[1] < pontoDivisor[1]:
                print("divisa")
            else:
                print("divisa")