lista = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        if l ==0:
            num = int(input(f'Digite um valor para {l,c}:'))
            lista[0].append(num)
        elif l == 1:
            num = int(input(f'Digite um valor para {l, c}:'))
            lista[1].append(num)
        elif l == 2 :
            num = int(input(f'Digite um valor para {l, c}:'))
            lista[2].append(num)
print(f'{lista[0]}')
print(f'{lista[1]}')
print(f'{lista[2]}')