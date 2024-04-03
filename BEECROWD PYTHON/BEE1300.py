while True:
    try:
        a = int(input())
        print("Y" if a %6 == 0 else "N")
    except EOFError:
        break