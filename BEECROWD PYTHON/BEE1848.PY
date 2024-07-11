resultado = 0
frase = ""

for c in range(3):
    while(True):
        frase = str(input())
        if frase == "caw caw":
            print(resultado)
            break
        elif frase=="---":
            resultado+=0
        elif frase=="--*":
            resultado+=1
        elif frase=="-*-":
            resultado+=2
        elif frase=="-**":
            resultado+=3
        elif frase=="*--":
            resultado+=4
        elif frase=="*-*":
            resultado+=5
        elif frase=="**-":
            resultado+=6
        elif frase=="***":
            resultado+=7       
    frase = ""
    resultado = 0