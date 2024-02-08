def contador(inicio,fim,passo):
    if inicio < fim:
        print(f'contagem de {inicio} até {fim} de {passo} em {passo} A')
        for d in range (inicio,fim+1,passo):
            print(d,end='')
        print(' Fim')
    else:
        print(f'contagem de {inicio} até {fim} de {passo} em {passo}')
        for e in range (inicio , fim-1,passo):
            print(e,end='')
        print(' Fim')

print(f'contagem de 1 até 10 de 1 em 1')
for d in range (1,11,1):
    print(d,end='')
print(' Fim')
print(f'contagem de 10 até 0 de 2 em 2')
for d in range (10,-1,-2):
    print(d,end='')
print(' Fim')
print('--' * 20)
print(f'personalize a contagem')
inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('Passo:'))
contador(inicio,fim,passo)