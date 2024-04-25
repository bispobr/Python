notas_Validas = []
while True:
    nota = float(input())
    if nota >= 0 and nota <=10:
        notas_Validas.append(nota)
    else:
        print("nota invalida")
    if len(notas_Validas) > 1:
        break
print(f"media = {(notas_Validas[0] + notas_Validas[1])/2:.2f}")
