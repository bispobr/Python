T = int(input())
valores = [int(x) for x in input().strip().split(' ')]

corretos = sum([1 for x in valores if x == T])

print(corretos)