fatorial = [40320, 5040, 720, 120, 24, 6, 2, 1]

N = int(input())

resultado = 0
for c in fatorial:
    resultado += N//c
    N %= c

print(resultado)