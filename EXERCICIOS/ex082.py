lista = []
resp = 'S'
while resp == 'S':
    lista.append(int(input('Digite um valor:')))
    resp = str(input("deseja continuar [S/N]")).upper()
listaP = []
listaI = []
for c in range(0,len(lista)):
    if lista[c]%2==0:
        listaP.append(lista[c])
    else:
        listaI.append(lista[c])
print(f'Lista Original : {lista}')
print(f'Lista valores Pares : {listaP}')
print(f'Lista valores Impares : {listaI}')