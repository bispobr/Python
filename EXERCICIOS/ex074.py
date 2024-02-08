import random
num = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
print(f'os valores sorteados foram {num}')
maior = menor = num[0]
for c in num:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c

print(f'maior Numero {maior}')
print(f'menor Numero {menor}')
