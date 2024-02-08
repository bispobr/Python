n1 = int(input("Primeiro termo:"))
ra = int(input("Razão da PA:"))
t2=t=1
mais = 1
while t <= 10:
    print(n1, end=">")
    n1+=ra
    t+=1
print("pausa")
n2 = n1

while mais !=0:
    mais = int(input("Quantos termos você quer mostrar a mais:"))
    while t2 <=mais:
        print(n2,end=">")
        n2+=ra
        t2+=1
    t2 = 1

print("fim")