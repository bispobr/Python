n = int(input())
l = [int(x) for x in input().split()]

for c in range(2, 6):
    multiplos = 0
    for nun in l:
        if nun % c == 0:
            multiplos += 1
        
    print(f"{multiplos} Multiplo(s) de {c}")
