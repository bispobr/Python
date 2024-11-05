from collections import deque

n = int(input())

for c in range(n):
    mina = input().strip()

    resposta = 0
    pilha = deque()
    for letra in mina:
        if(letra == '<'):
            pilha.append('<')
        elif(letra == '>' and len(pilha) > 0):
            resposta += 1
            pilha.pop()
    
    print(resposta)