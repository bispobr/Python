linhas = int(input())
inicio = 1
for d in range(0,linhas):
    for c in range (inicio, inicio + 3):
        print(c,end=" ")
    print("PUM")
    inicio+=4
