lista = []
resp = 'S'
while resp == 'S':
    lista.append(int(input('Digite um valor:')))
    resp = str(input('Deseja Continuar [S/N]:')).upper()
if 5 in lista:
    msg = "O valor 5 faz parte da lsita!"
else:
    msg = "O valor 5 NAO faz parte da lsita!"
print(f'Quantidade de numeros Digitados :{len(lista)}')
lista.sort(reverse=True)
print(f'lista de valores, ordenada de forma decrescente: {lista}')
print(msg)
