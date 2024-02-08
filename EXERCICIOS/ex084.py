pessoas = []
dados = []
resp = "S"
totpessoa = 0
maiorpeso = 0
menorpeso= 999999
while resp == "S":
    nome = str(input('Nome:'))
    peso = int(input('peso:'))
    pessoas.append(nome)
    pessoas.append(peso)
    dados.append(pessoas[:])
    pessoas.clear()

    resp = str(input('Quer continuar? [S/N]')).upper()
for c in dados:
    print(c)
    totpessoa +=1
    if c[1] >= maiorpeso:
        maiorpeso = c[1]
    elif c[1]<= menorpeso:
        menorpeso = c[1]
print(f'Total de pessoas Cadastradas {totpessoa}')
print(f'o maior peso foi de {maiorpeso} kg')
print(f'o menor peso foi de {menorpeso} KG')

for d in dados:
    if d[1] == maiorpeso:
        print(f'Listagem de pessoas com maiores pesos : {d[0]}')
for e in dados:
    if e[1] == menorpeso:
        print(f'Listagem de pessoas com menores pesos : {e[0]}')