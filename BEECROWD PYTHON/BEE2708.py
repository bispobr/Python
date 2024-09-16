jipes = 0
salida = 0

while True:
    passeio = [str (x) for x in input().split()]

    if passeio[0] == "ABEND":
        break
   
    if passeio[0] == "SALIDA":
        salida += int(passeio[1])
        jipes +=1  
    elif passeio[0] == "VUELTA":
        salida -= int(passeio[1])
        jipes -=1

print(salida)
print(jipes)