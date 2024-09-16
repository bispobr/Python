minutos =int(input())
presentes = [int(x) for x in input().split()]

if sum(presentes)<= minutos:
    print("Farei hoje!")
else :
    print("Deixa para amanha!")