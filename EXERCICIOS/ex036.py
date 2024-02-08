casa = int(input("Qual o valor da casa R$:"))
salario = int (input("qual o salario do comprador R$:"))
parcelas = int(input("Quantidade de anos:"))
valorMes = casa / (parcelas * 12)
psalario = (salario*30)/100
print("Para pagar uma casa de R$ {:.2f} em {} a prestação será de R${:.2f}".format(casa,parcelas,valorMes))

if psalario >= valorMes:
    print('Emprestimo aprovado!!!')
else:
    print("Emprestimo Negado!!!")
