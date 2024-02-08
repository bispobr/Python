n1 = int(input("Digite o primerio numero:"))
n2 = int(input("Digite o segundo numero:"))
sair = False
while not sair:
    print("[ 1 ] somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4] Novos numeros")
    print("[ 5 ] Saior do programa")
    op: int=int(input("qual é a sua opção:"))

    if op==1:
        s=n1+n2
        print("----------------------------------------------------------")
        print("A soma dos valores {} e {} é : {}".format(n1,n2,s))
        print("----------------------------------------------------------")
    elif op==2:
        m= n1 * n2
        print("----------------------------------------------------------")
        print("A Multiplicação dos valores {} e {} é : {}".format(n1, n2, m))
        print("----------------------------------------------------------")
    elif op==3:
        if n1>n2:
            print("----------------------------------------------------------")
            print(" O numero {} é maior".format(n1))
            print("----------------------------------------------------------")
        else:
            print("----------------------------------------------------------")
            print(" O numero {} é maior".format(n2))
            print("----------------------------------------------------------")
    elif op==4:
        print("----------------------------------------------------------")
        n1 = int(input("Digite o primerio numero:"))
        n2 = int(input("Digite o segundo numero:"))
        print("----------------------------------------------------------")
    elif op==5:
        sair=True
