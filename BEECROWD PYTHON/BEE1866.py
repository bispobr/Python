casos = int (input())

for c in range(casos):
    termo = int (input())
    s = 0
    for c in range(termo):

        if c % 2 == 0:
            s+=1
        else :
            s-=1
    print(s)