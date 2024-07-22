casos  = int(input())

for c in range(casos):
    j1,e1,j2,e2 = str(input()).split()
    valores = [int(x) for x in input().strip().split(' ')]
    resultado= sum(valores) % 2 

    if resultado == 0:
         if e1 == "PAR":
              print(j1)
         elif e2 == "PAR":
              print(j2)
              
    else :
         if e1 == "IMPAR":
              print(j1)
         elif e2 == "IMPAR":
              print(j2)