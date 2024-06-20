x=[]

for c in range (10):
   valor = int(input())
   x.append(valor)

for e in range (10):
    if x[e] <=0:
        x[e] = 1


for d in range (10):
    print("X[{}] = {}".format(d,x[d]))