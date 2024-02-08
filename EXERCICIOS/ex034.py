sal = float (input("Qual é o salario:"))
if sal <= 1250 :
 novo = sal + ((sal * 15)/100)
else:
    novo = sal + ((sal *10)/100)
print("O seu novo salario e de R$ {}".format(novo))

