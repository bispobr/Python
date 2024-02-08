fim = int(input("Quantos Termmos voce quer mostrar:"))
c=3
p1=0
p2=1
print("{}>{}".format(p1,p2),end=">")
while c<= fim:
    ultimo =p1 + p2
    print(ultimo, end=">")
    p1 = p2
    p2 = ultimo
    c+=1
print("fim")
print("Tentar fazer depos!!!!")