t = int(input())

for c in range (t):
    conversao = str(input())
    r,g,b = [int (x) for x in input().split()]

    if conversao == "eye":
        p = int(((r * 30)/100) + ((g * 59)/100) + ((b * 11)/100))
    elif conversao == "mean":
        p = int((r+g+b)/3)
    elif conversao == "max":
        p = max(r,g,b)
    elif conversao == "min":
        p = min(r,g,b)

    print(f'Caso #{c + 1}: {p}')