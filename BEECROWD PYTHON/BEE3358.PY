n = int(input())
for i in range(n):
    sobrenome = input()
    dificil = False
    
    tam = len(sobrenome) - 2
    
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for l in range(tam):
        if sobrenome[l] not in vogais:
            if sobrenome[l + 1] not in vogais:
                if sobrenome[l + 2] not in vogais:
                    dificil = True
   

    if dificil :  
        print(f"{sobrenome} nao eh facil") 
    else: 
        print(f"{sobrenome} eh facil")
            
           