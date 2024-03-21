cont = 0
soma = 0
for c in range (1,7):
    valor = float(input())
    if (valor >= 0):
        cont = cont + 1
        soma = soma + valor

print("{} valores positivos".format(cont))
print("{:.1f}".format(soma/cont))

