resp = 0
n = int(input())
for c in range (n):
    l,c  = [int (x) for x in input().split()]
    if l > c:
        resp += c
print(resp)
