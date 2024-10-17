categorias=[1, 3, 5, 10, 25, 50,100]
k=int(input())

for c in range(7):
    if k<=categorias[c]:
        print(f"Top {categorias[c]}")
        break

