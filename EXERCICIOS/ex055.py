maior = 0
menor = 99999
for c in range (1,6):
    peso = float(input("Digite o peso da pessoa {} :".format(c)))
    if peso >maior:
        maior = peso
    if peso < menor:
        menor = peso
print("maior pseso: {}".format(maior))
print("Menor peso: {}".format(menor))