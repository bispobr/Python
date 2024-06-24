n = []

for c in range(20):
    valor = int(input())
    n.append(valor)

n.reverse()

for d in range(len(n)):
    print("N[{}] = {}".format(d,n[d]))