lista = []
for c in range (0,5):
    num= int(input(f"Digite o valor {c}:"))
    if len(lista) == 0 or  num > lista[-1] :
        lista.append(num)
    else:
        pos = 0
        while pos<len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(f'valores na lista {lista}')