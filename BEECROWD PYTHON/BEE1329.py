while True:
    n = int(input())
    if n==0:
        break
    resultdo = [int(x) for x in str(input()).split()]
    maria = 0
    joao = 0
    for c in range(n):
        if resultdo[c] == 0:
            maria+=1
        elif resultdo[c] == 1:
            joao+=1

    print("Mary won {} times and John won {} times".format(maria,joao))


