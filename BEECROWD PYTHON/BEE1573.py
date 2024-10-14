import math
while True:
    a, b, c = [int(x) for x in input().split()]

    if a == b == c == 0:
        break

    print(math.floor((a * b * c)**(1.0/3.0)))
