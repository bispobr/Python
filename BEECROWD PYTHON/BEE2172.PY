while True:
    try:
        x, m = [int(x) for x in input().split()]

        if x == 0 and m == 0:
            break

        print(m * x)
    except EOFError:
        break
