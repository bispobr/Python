resp = "S"
lista = []
while resp =='S':
    num = (int(input('Digite um valor:')))
    if num in lista:
        print('Valor duplicado! não vou adicionar...')
    else:
        print('Valor Adicionado com sucesso...')
        lista.append(num)
    print('Deseja continuar:')
    resp = (str(input('Deseja Continuar [S/N] :'))).upper()
lista.sort()
print(f'valores na lista {lista}')