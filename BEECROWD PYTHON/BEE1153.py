def fibo(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    print(ans)

n = int(input())
fibo(n)
