somap = 0
for c in range (1,7):
    num =int(input("{} Digite o numero: ".format(c)))
    if num % 2 == 0:
        somap += num
print("Soma dos numeros pares {}".format(somap))