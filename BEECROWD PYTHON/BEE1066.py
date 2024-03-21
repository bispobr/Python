contP = contI = pos= neg = 0
for c in range (0,5):
    valor = int(input())
    if valor % 2 == 0:
        contP +=1
    else:
        contI +=1

    if valor > 0:
        pos += 1
    elif valor < 0:
        neg += 1

print("{} valor(es) par(es)".format(contP))
print("{} valor(es) impar(es)".format(contI))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))