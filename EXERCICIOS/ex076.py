lista = ("lapis",1.75,"carne",5.75,"lanterna",9.56,"controle",45.75,"mouse",9.75,)
for c in range(0, len(lista),2):
    print("{}.................... R${}".format(lista[c],lista[c+1]))