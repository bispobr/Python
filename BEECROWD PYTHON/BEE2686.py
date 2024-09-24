def graus_para_hhmmss(graus):
    horas = int(graus / 15) + 6
    if horas == 24:
        horas = 0
    elif horas >24:
        horas = horas - 24
    minutos = int((graus % 15) * 4)
    segundos = int(((graus % 15) * 4 - minutos) * 60)
    
    return f"{horas:02}:{minutos:02}:{segundos:02}"

while True:
    try: 
        entrada = float(input())
        
        if entrada == 360:
            print("Bom Dia!!")
        if entrada >=0 and entrada < 90:
            print("Bom Dia!!")
        elif entrada >=90 and entrada < 180:
            print("Boa Tarde!!")
        elif entrada >=180 and entrada < 270:
            print("Boa Noite!!")
        elif entrada >=270 and entrada < 360:
            print("De Madrugada!!")

        print(graus_para_hhmmss(entrada))
    except EOFError:
        break
