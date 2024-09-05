while True:
    try:
        casos = int(input())
        impeachment = (casos / 3) * 2 
        votos = [int (x) for x in input().split()] 
        print("impeachment" if sum(votos) >= impeachment else "acusacao arquivada")      
    except EOFError:
        break