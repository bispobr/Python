a = []

for c in range(100):
    valor = float (input())
    a.append(valor)

for d in range(100):
    if a[d] <= 10:
        print("A[{}] = {}".format(d,a[d]))

