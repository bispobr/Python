N = int(input())
for c in range(N):
    X = int(input())

    resp, cont = 0, 0
    while(X > 0):
        if(X % 2 == 1):
            cont += 1
        else:
            resp = max(resp, cont)
            cont = 0
        X //= 2
    resp = max(resp, cont)

    print(resp)