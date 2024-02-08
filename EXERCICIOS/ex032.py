ano = int(input("Qual ano quer analisar?"))
if ano%4 == 0 and ano%100 !=0 or ano%400 == 0:
    print("è um ano Bissexto")
else:
    print("Não é um ano bissexto")