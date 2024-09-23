n = int(input())
palavras = []

for c in range(n):
    palavras.append(str(input()))

q = int(input())

for c in range(q):
    cont = 0
    maior = 0
    busca = str(input())
    for d in range(len(palavras)):
       if  palavras[d].startswith(busca):
           cont +=1
           if len(palavras[d]) > maior:
            maior = len(palavras[d])
    if cont > 0:
         print(f'{cont} {maior}')
    else :
        print(-1)