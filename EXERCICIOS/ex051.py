n1 = int(input("Primeiro termo:"))
ra = int(input("Razão da PA:"))
decimo = n1 + (10-1) * ra
for c in range(n1,decimo + ra,ra):
    print(c, end=">")