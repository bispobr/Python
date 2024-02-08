lista = [[],[]]
for c in range(0,7):
    num = int(input(f'Digite o valor {c}:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Valores pares: {sorted(lista[0])}')
print(f'valores impares: {sorted(lista[1])}')





