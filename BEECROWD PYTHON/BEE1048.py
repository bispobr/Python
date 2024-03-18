valor = float(input())

if valor > 0 and valor <= 400.00:
    percentual = 15
    reajuste = (valor * percentual) / 100
    nsalario = valor + reajuste
elif valor >= 400.01 and valor <= 800.00:
    percentual = 12
    reajuste = (valor * percentual) / 100
    nsalario = valor + reajuste
elif valor >= 800.01 and valor <=1200.00:
    percentual = 10
    reajuste = (valor * percentual) / 100
    nsalario = valor + reajuste
elif valor >= 1200.01 and valor <= 2000.00:
    percentual = 7
    reajuste = (valor * percentual) / 100
    nsalario = valor + reajuste
elif valor > 2000.00:
    percentual = 4
    reajuste = (valor * percentual) / 100
    nsalario = valor + reajuste

print("Novo salario: {:.2f}".format(nsalario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))