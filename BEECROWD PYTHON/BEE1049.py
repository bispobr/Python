palavra1 = str(input())
if palavra1 == "vertebrado":
    palavra2 = str(input())
    if palavra2 == "ave":
        palavra3 = str(input())
        if palavra3 == "carnivoro":
            print("aguia")
        elif palavra3 == "onivoro":
            print("pomba")
    elif palavra2 == "mamifero":
        palavra3 = str(input())
        if palavra3 == "onivoro":
            print("homem")
        elif palavra3=="herbivoro":
            print("vaca")
elif palavra1 == "invertebrado":
    palavra2 = str(input())
    if palavra2 == "inseto":
        palavra3 = str(input())
        if palavra3 == "hematofago":
            print("pulga")
        elif palavra3 == "herbivoro":
            print("lagarta")
    elif palavra2 == "anelideo":
        palavra3 = str(input())
        if palavra3 == "hematofago":
            print("sanguessuga")
        elif palavra3 == "onivoro":
            print("minhoca")