n = int(input())
for c in range(n):
    golpe= input()
    posicao = golpe.find("k")
    
    quantidade1 = golpe[:posicao].count("a")
    quantidade2 = golpe[posicao:].count("a")
    
    print("k", end="")
    print("a" * (quantidade1 * quantidade2))
   
