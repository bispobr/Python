from datetime import date
maioridade = 0
menoridade = 0
for c in range (1,8):
    nasc = int(input("{} ano de nascimento:".format(c)))
    idade = date.today().year - nasc
    if idade >= 21:
        maioridade +=1
    else:
        menoridade +=1
print("Pessoas maior idade {}".format(maioridade))
print("Pessoas menor idade {}".format(menoridade))