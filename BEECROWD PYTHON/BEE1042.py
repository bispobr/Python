valores = [int(x) for x in input().strip().split(' ')]
v = valores[:]
v.sort()

for c in v:
    print(c)
print()
for c in valores:
    print(c)