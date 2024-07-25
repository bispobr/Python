
while True:
    try:
        V = float(input())
        D = float(input())

        D /= 2

        area = 3.14 * D * D
        altura = V / area

        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')
    except EOFError:
        break