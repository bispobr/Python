import math

a = 1
while (a != 0):
    try:
        a,b,c = [int (x) for x in str(input()).split()]

        print(f"{(math.floor(math.sqrt(a * b * 100.0 / c))):.0f}")
    except ValueError:
        break