num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
num3 = int(input("Digite o terceiro numero"))

if num1 > num2:
    maior = num1
if num2 > num1:
    maior = num2
if num3 > maior:
     maior = num3

if num1 < num2 :
    menor = num1
if num2 < num1 :
    menor = num2
if num3 < menor :
    menor = num3

print("O Maior valor digitado foi {}".format(maior))
print("O menor valor Digitado Foi {}".format(menor))

