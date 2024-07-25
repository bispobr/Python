casos = int(input())

for c in range(casos):
    A = str(input())
    B = str(input())

    if (A == "ataque" and  B == "ataque"):
        print("Aniquilacao mutua")
    elif (A == "pedra" and B == "pedra") :
        print("Sem ganhador")
    elif (A == "papel" and B == "papel") :
        print("Ambos venceram")
    elif (A == "ataque") :
        print("Jogador 1 venceu")
    elif (B == "ataque") :
        print("Jogador 2 venceu")
    elif (A == "pedra") :
        print("Jogador 1 venceu")
    elif (B == "pedra") :
        print("Jogador 2 venceu")
    
