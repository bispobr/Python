valores = list()
for c in range(0,100):
    valores.append(int(input()))

print(max(valores))
print(1 + (valores.index(max(valores))))