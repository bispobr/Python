while True:
    num = int(input("Quer a tabuada de qual numero::"))
    if num <0:
        break
    for c in range (1,11):
        print(f'{num} x {c} = {num*c}')

