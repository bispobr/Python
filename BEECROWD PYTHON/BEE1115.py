def quadrante(x,y):
    if x > 0:
        if y > 0:
            msg = f"primeiro"
        else:
            msg = f"quarto"
    elif x < 0:
        if y > 0:
            msg = f"segundo"
        else :
            msg = f"terceiro"
    return msg

while True:
    x,y = [int (x) for x in str(input()).split()]
    if x == 0 or y ==0:
        break
    print(quadrante(x,y))
