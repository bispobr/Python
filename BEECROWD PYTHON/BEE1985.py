total = 0

qtd = int(input())

for c in range (qtd):
    p,q = [int(x) for x in input().strip().split(' ')]

    match p:
       case 1001:
         total += q * 1.50
       case 1002:
         total += q * 2.50
       case 1003:
         total += q * 3.50
       case 1004:
         total += q * 4.50   
       case 1005:
         total += q * 5.50      

print(f'{total:.2f}')