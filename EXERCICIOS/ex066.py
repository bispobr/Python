n=s=c=0
while True:
    n = int(input("digite um valor[999 para parar]:"))
    if n == 999:
        break
    c+=1
    s+=n
print("foram Digitados {}".format(c ))
print("A soma dos numeros digitados é {}".format(s))