c = 1
while True:
    v = int(input())

    if v == 0:
        break

    print(f"Teste {c}")
    
    i = v // 50
    resto = v%50
    j = resto // 10
    resto = resto%10
    k = resto // 5
    resto = resto%5
    l = resto// 1
    c+=1
    print(f"{i} {j} {k} {l}")
    print()
    