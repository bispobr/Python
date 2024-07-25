a,b,c = [int(x) for x in input().strip().split(' ')]

if a == 0:
    h = 24 + (b + c)
else:
    h = a + (b + c)


if h == 24:
    print(0)
elif h >24:
    print(f"{h - 24}")
else:
    print(f"{h}")
