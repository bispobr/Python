alcool = gasolina = diesel = 0
while True:

    op = int(input())

    if (op == 1):
        alcool +=1
    elif (op == 2):
        gasolina +=1
    elif (op == 3):
        diesel +=1
    elif (op == 4):
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")