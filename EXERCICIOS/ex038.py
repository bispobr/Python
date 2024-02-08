valor1 = int(input("digite o valor 1 :"))
valor2 = int(input("digite o valor 2:"))
if valor1 > valor2:
    print("Valor 1 {} é maior que valor2 {}".format(valor1,valor2))
elif valor2 > valor1:
    print("valor2 {} é maior que o valor1 {}".format(valor2, valor1))
elif valor1 == valor2:
    print(" os valores são iguais!!!")