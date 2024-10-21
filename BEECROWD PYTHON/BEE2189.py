d = 1
while True:
    v = int(input())

    if v == 0:
        break
    
    participantes = [int (x) for x in input().split(" ")]

    print(f"Teste {d}")
    d+=1
    for c in range (v):
        if participantes[c] == c + 1:
            print(participantes[c])
            print()
            
    
   
    
   