par = []
impar = []

for c in range(15):
    valor = int(input())

    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    if len(par) == 5:
        for c in range(5):
           print("par[{}] = {}".format(c,par[c])) 
        par.clear()

    if len(impar) == 5:
        for d in range(5):
           print("impar[{}] = {}".format(d,impar[d])) 
        impar.clear()

for d in range(len(impar)):
           print("impar[{}] = {}".format(d,impar[d])) 

for c in range(len(par)):
           print("par[{}] = {}".format(c,par[c])) 

