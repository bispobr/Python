casos_de_Teste = int(input())
total_coelhos =total_rato=total_sapo= 0
for c in range(casos_de_Teste):
    quantia,tipo = str(input()).split()
    if tipo == "C":
        total_coelhos += int(quantia)
    elif tipo == "R":
        total_rato+= int(quantia)
    elif tipo == "S":
        total_sapo += int(quantia)

total_cobaias = (total_rato + total_sapo + total_coelhos)
percentual_de_coelhos = (total_coelhos * 100)/total_cobaias
percentual_de_ratos = (total_rato * 100)/total_cobaias
percentual_de_sapos = (total_sapo * 100)/total_cobaias

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_rato}')
print(f'Total de sapos: {total_sapo}')
print("Percentual de coelhos: {:.2f} %".format(percentual_de_coelhos))
print("Percentual de ratos: {:.2f} %".format(percentual_de_ratos))
print("Percentual de sapos: {:.2f} %".format(percentual_de_sapos))

