valores = str(input()).split()
a = float (valores[0])
b = float (valores[1])
c = float (valores[2])

if ((a < b + c) and (b < a + c) and (c < a + b)):

    print("Perimetro = {:.1f}".format(a + b + c))
else:
    area = ((a + b)/2)*c
    print("Area = {:.1f}".format(area))