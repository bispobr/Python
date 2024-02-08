n1 = int(input("Digite um numero:"))
div = 0
for c in range (1,n1 + 1):
        if n1%c == 0:
                div +=1
if div>2:
        print("O numero {} foi Dividido {},NÃO É UM NUMERO PRIMO!!!".format(n1,div))
else:
        print("O Numero {} foi dividido {},É UM NUMERO PRIMO!!!".format(n1,div))