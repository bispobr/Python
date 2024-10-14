def switch(valor):
    match valor:
        case 1:
            print("Rolien") 
        case 2:
            print("Naej")
        case 3:
            print("Elehcim")
        case _:
            print("Odranoel")

n = int(input())

for a in range(n):
    k = int(input())        
    for c in range (k):
        op=int(input())
        switch(op)
    