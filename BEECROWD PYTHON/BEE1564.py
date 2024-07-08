while True:
    try:
        n = int(input())
        print( "vai ter duas!"if n>0 else "vai ter copa!")
    except EOFError:
        break