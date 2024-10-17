n = int(input())
la,lb = [int (x) for x in input().split()]
sa,sb = [int (x) for x in input().split()]

print("possivel" if (n >= la and n<=lb ) and (n >= sa and n <= sb) else "impossivel")