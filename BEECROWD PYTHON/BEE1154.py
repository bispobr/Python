idade = 999
soma = 0
cont = 0

while (idade > 0):

    idade = int(input())

    if idade > 0:
       cont +=1
       soma += idade

print(f"{soma / cont:.2f}")
