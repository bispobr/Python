n = int(input())
p,c, q=[str (x) for x in input().split()]

if c == "+":
    print("OK" if int(p)+int(q) <=n else "OVERFLOW")
elif c== "*":
    print("OK" if int(p)*int(q) <=n else "OVERFLOW")
    

