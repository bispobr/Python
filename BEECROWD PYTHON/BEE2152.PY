casos = int(input())

for c in range(casos):
    hora, minuto, porta = [int(x) for x in input().split()]
    print(f'{hora:02d}:{minuto:02d} - { "A porta abriu!" if porta == 1 else "A porta fechou!"}')
