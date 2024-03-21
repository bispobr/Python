x = int(input())
y = int(input())
soma = 0
maior  = max(x,y)
menor = min(x,y)
for c in range (menor + 1,maior):
    if c % 2 != 0:
        soma = soma + c

print(soma)