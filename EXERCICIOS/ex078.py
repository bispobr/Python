num = []
for c in range(0,5):
    num.append(int(input('Digite uma valor:')))
print(f'Maior valor {max(num)} na posições listadas  abaixo ')
for d in range (0,5):
    if  num[d] == max(num):
       print(d)
print(f'menor valor {min(num)} nas posições listadas  abaixo')
for d in range (0,5):
    if  num[d] == min(num):
       print(d)


