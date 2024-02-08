lista = [[0,0,0],[0,0,0],[0,0,0]]
somap = somavc=ml =maior= 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite os valores para [{l},{c}] :'))

print(f'{lista[0]}')
print(f'{lista[1]}')
print(f'{lista[2]}')

for l in range(0,3):
    somavc += lista[l][2]
    if  lista[1][l] > maior:
        maior =lista [1][l]
    #print(f'Valor : {lista[l][2]}')
    for c in range(0,3):
        if lista[l] [c] % 2==0:
            somap += lista[l] [c]


print(f'Soma dos Valores pares: {somap}')
print(f'soma dos valores da terceira coluna : {somavc} ')
# forma tradicional
print(f'O maior valor da segunda linha: {max(lista[1])} ')
# forma simplificada
print(f'O maior valor da segunda linha: {maior}')
