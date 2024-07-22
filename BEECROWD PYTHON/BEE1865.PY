casos = int (input())

for c in range(casos):
    nome, forca = str(input()).split()
    print('Y' if nome == 'Thor' else 'N')