pessoa = dict()
lista = list()
while True:
    pessoa['nome'] = str(input("Nome:"))
    pessoa['sexo'] = str(input("Sexo:")).upper()
    pessoa['idade']= int(input("Idade:"))
    resp = str(input("Deseja continuar: [S/N] ")).upper()
    lista.append(pessoa.copy())
    pessoa.clear()
    if resp == "N":
        break

somaI = 0
for c in range (0,len(lista)):
    somaI += lista [c]['idade']
media = somaI / len(lista)

print(("**")*25)
print(f'Quantidade de pessoas cadastradas {len(lista)}')
print(f'média de idade : {media} anos')
print("****listagem de mulheres ****")
for c in range (0,len(lista)):
    if lista[c]['sexo'] == 'F':
        print(lista [c]['nome'])
print("****Pessoas com idade acima da media ****")
for c in range (0,len(lista)):
    if lista[c]['idade'] > media:
        print(lista [c])


