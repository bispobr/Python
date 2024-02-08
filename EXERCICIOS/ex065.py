s=cont=maior=menor=0
op="s"
while  op == "s":
    num = int(input("Digite o numero:"))
    s+=num
    cont+=1
    if cont == 1:
        maior=menor=num
    else:
        if num > maior:
             maior = num
        if num < menor:
          menor = num
    op = str(input("Deseja continuar [s/n]:"))
print("A media dos valores digitados foi {}".format(s/cont))
print("Maior valor : {}".format(menor))
print("Menor Valor {}".format(menor))
