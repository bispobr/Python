casos = int(input())

for c in range(casos):
    nome = str(input())
    grau = float(input())
    notas = [float (x) for x in input().split()]
    nota = (sum(notas) - min(notas) - max(notas)) * grau

    print(f'{nome} {nota:.2f}')