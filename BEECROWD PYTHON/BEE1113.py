def ordem(x,y):
    if x > y:
        msg = f"Decrescente"
    else:
        msg = f"Crescente"
    return msg

while True:
    x,y = [int (x) for x in str(input()).split()]
    if x == y:
        break
    print(ordem(x,y))


