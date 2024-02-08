km = float(input("Qual a Distancia DA Viagem em KM:"))
if km <= 200 :
    preco1 = km * 0.50
    print("O preço da passagem  sera de R$ {:.2f}".format(preco1))
else:
    preco2 = km * 0.45
    print("O preço da passagem sera de R$ {:.2f}".format(preco2))