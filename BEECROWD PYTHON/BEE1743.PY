tomada1= [int(x) for x in input().split()]
tomada2= [int(x) for x in input().split()]

compativel=True

for c in range(len(tomada1)):
    if tomada1[c]==tomada2[c]:
        compativel= False
        break

print("Y" if compativel else "N")
