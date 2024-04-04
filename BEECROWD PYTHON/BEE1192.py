n = int(input())
for c in range (n):
    frase = str(input())
    d1 = int(frase[0])
    d2 = int(frase[2])
    if d1 == d2:
        print(d1 *d2)
    elif "A" <= frase[1] <= "Z":
        print(d2 - d1)
    else:
        print(d1 + d2)
