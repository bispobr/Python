n=s=c=0
n = int(input("digite um valor[999 para parar]:"))
while n !=999:
    c+=1
    s+=n
    n = int(input("digite um valor[999 para parar]:"))
print("foram Digitados {}".format(c ))
print("A soma dos numeros digitados é {}".format(s))