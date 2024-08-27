casos = int(input())

stotoal = 0
btotal = 0
atotal  = 0
s1totoal = 0
b1total = 0
a1total  = 0

for c in range (casos):
    nome = input()
    s,b,a = [int (x) for x in input().split()]
    stotoal += s
    btotal += b
    atotal += a
    
    s1,b1,a1 = [int (x) for x in input().split()]
    s1totoal += s1
    b1total += b1
    a1total += a1

print(f'Pontos de Saque: {100 * s1totoal/stotoal:.2f} %.')
print(f'Pontos de Bloqueio: {100 * b1total/btotal:.2f} %.')
print(f'Pontos de Ataque: {100 * a1total/atotal:.2f} %.')
    
