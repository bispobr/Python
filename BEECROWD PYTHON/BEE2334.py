while True:
    try:
        p = int(input())

        if p == -1:
            break

        print(0 if p == 0 else p - 1)

    except EOFError:
        break