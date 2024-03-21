cont = 0
for c  in range (1,6):
    valor = int(input())
    if valor % 2 ==0:
        cont +=1
print("{} valores pares".format(cont))