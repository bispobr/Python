compra = float(input("Preço das compras R$:"))
print("FORMAS DE PAGAMENTO")
print("[1] á vista dinheiro/cheque")
print("[2] á vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
op = int(input("Opção escolhida:"))
if op == 1:
    op1 = (compra) - ((compra * 10) / 100)
    print("sua compra de R$ {:.2f} vai custar R${:.2f} no final".format(compra,op1))
elif op == 2:
    op2 = (compra) - ((compra * 5) / 100)
    print("Sua compra de R$ {:.2f} vai custar R${:.2f} no final ".format(compra,op2))
elif op == 3:
        print("sua compra vai ser parcelada em 2x de R$ {}".format(compra / 2))
        print('Sua compra vai ser R$ {:.2f}'.format(compra))
elif op == 4:
    parcelas = int(input('Quantidade de parcelas:'))
    op3 = (compra) + ((compra * 20) / 100)
    op4 = op3 / parcelas
    print('Sua comra sera percelada em {}x de R$ {:.2f}'.format(parcelas,op4))
    print('Sua compra de R$ {:.2f} vai custar {:.2f}'.format(compra,op3))
else:
    print('Opção invalida de pagamento!!!')