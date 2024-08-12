resposta = 0
n = int(input())
r = [int (x) for x in input().strip().split(' ')]
for i in range(1, n):
    if(r[i] < r[i - 1]):
        resposta = i + 1
        break

print(resposta)