andares = []

for c in range(3):
    andares.append(int(input()))

print(2 * min(andares[1]+ 2 * andares[2], andares[0] + andares[2], 2 * andares[0] + andares[1]))