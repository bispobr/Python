n = int(input())
classificados = int (input())
notas = []

for c in range (n):
    notas.append(int(input()))  

notas.sort()

for c in range (classificados):
    ultimo = notas.pop()

print(notas.count(ultimo) + classificados)



