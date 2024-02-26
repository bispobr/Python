import math
v1 = str(input()).split()
v2 = str(input()).split()
x1 = float(v1[0])
y1 = float(v1[1])
x2 = float(v2[0])
y2 = float(v2[1])
distancia = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
print('{:.4f}'.format(distancia))


