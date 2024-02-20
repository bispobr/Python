valores = str(input()).split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
triangulo = (a*c) /2
circ = 3.14159 * c**2
tra = ((a + b) /2)*c
qua = b**2
ret = a*b
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circ))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))