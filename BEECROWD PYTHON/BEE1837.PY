import math
a,b = [int (x) for x in str(input()).split()]


if a > 0:
    if b > 0:
        q = math.floor(a/b)
    else:
        q = math.ceil(a/b)
else:
    if b > 0:
        q = math.floor(a/b)
    else:
        q = math.ceil(a/b)

print ("{} {}".format(q,a -(b * q)))