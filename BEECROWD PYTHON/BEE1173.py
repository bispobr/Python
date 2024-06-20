n=[]
valor = int(input())
n.append(valor)

for c in range (9):
    n.insert(c+1,n[c] * 2)

for d  in range (10):
    print("N[{}] = {}".format(d,n[d]))



