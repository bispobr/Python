n = []
valor = float(input())
n.append(valor)

for c in range (99):
    n.insert(c+1 , n[c] / 2)
    
for d in range (100):
    print("N[{}] = {:.4f}".format(d,n[d]))