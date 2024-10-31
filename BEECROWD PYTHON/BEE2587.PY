n = int(input())
for c in range(n):
    palavra1= input()
    palavra2= input()
    palavra3= input()
    
    inicio = palavra3.find("_")
    fim = palavra3.rfind("_")
    
    if palavra1[fim] == palavra2 [inicio]  or palavra1[inicio] == palavra2[fim]:
        print("Y")
    else:        
        print("N")