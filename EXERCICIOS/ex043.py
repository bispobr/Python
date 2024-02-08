peso = float(input("Digite o peso:"))
altura = float (input("Digite a  altura:"))
imc = peso /(altura * altura)
print("Imc :{:.1f}".format(imc))
if imc < 18.5:
    print("Abaixo do Peso")
elif imc <= 25.5:
    print("peso ideal")
elif imc <= 30:
    print("sobrepeso")
elif imc <= 40 :
    print("Obesidade")
elif imc > 40:
    print("Obesidade morbida")