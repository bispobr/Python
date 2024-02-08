from datetime import date
nasc = int(input("Ano de nascimento :"))
idade = date.today().year - nasc
print("Sua idade é {}".format(idade))
if idade <= 9:
    print("Categoria Mirim")
elif idade > 9 and idade <=14:
    print("categoria Infantil")
elif idade > 14 and idade <= 19:
    print("categoria Junior")
elif idade >19 and idade <= 25:
    print("categoria Senior")
elif idade > 25:
    print(" Categoria Master")
