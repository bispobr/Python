joias = []
while True:
    try: 
        entrada = str(input())
        if entrada not in joias:
            joias.append(entrada)
    except EOFError:
        break
print(len(joias))