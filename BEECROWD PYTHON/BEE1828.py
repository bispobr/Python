casos = int (input())

for c in range(casos):
    a,b = [ x for x in str(input()).split()]
    
    if (a == "tesoura" and b == "papel") or (a == "papel" and b == "pedra") or (a == "pedra" and b == "lagarto") or (a == "lagarto" and b == "Spock") or (a == "Spock" and b == "tesoura") or (a == "tesoura" and b == "lagarto") or (a == "lagarto" and b == "papel") or (a == "papel" and b == "Spock") or (a =="Spock" and b == "pedra") or (a == "pedra" and b == "tesoura"):
        resposta = "Bazinga!"
    elif (a ==b):
        resposta = "De novo!"
    else:
        resposta = "Raj trapaceou!"
    
   
    print("Caso #{}: {}".format(c+1,resposta)) 