x = int(input())
y = int(input())

if x > y:
    x,y = y,x

for c in range(x + 1,y ):
    if c % 5 == 2 or c % 5 == 3:
        print(c)