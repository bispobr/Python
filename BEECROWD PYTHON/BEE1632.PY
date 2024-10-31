n = int(input())

especiais = ["A","E", "I", "O" , "S","a","e", "i", "o" , "s"]

for c in range(n):
    senha = input()
    total= 1
    
    for c in range(len(senha)):

        if senha[c] in especiais:
            total *=3
        else:
            total *=2

    print(total)