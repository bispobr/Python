n =int (input())
valores = [int(x) for x in str(input()).split()]
print(valores.index(min(valores)) + 1)
