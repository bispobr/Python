salario = float(input())

if  salario >= 0.00 and salario <= 2000.00:
    print("Isento")
elif salario >= 2000.01 and salario <= 3000.00:
    imposto = (salario - 2000) * 0.08
    print ("R$ {:.2f}".format(imposto))
elif salario >=3000.01 and salario <= 4500.00:
    imposto = (salario - 3000) * 0.18 + 1000 * 0.08
    print ("R$ {:.2f}".format(imposto))
elif salario >=4500.00:
    imposto = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print ("R$ {:.2f}".format(imposto))
