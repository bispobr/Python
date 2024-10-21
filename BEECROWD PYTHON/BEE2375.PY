n = int(input())
b,c, d=[int (x) for x in input().split()]
print("S" if n  <= b and n <= c and n <= d else "N")