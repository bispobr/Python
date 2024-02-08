from random import randint

escolha = int(input("Em que numero eu pensei?"))
pc = randint(0,5)
cont = 1
while escolha != pc:
    cont+=1
    if escolha == pc:
        print("Tentativa {} : Parabens!!! Voce Acertou".format(cont))
    else:
         print("Voce errou o palpite, eu pensei no numero {}".format(pc))
    escolha = int(input("jogo {}: Em que numero eu pensei?".format(cont)))
    pc = randint(0, 5)
print("Parabens!!! Voce Acertou foram realizados {} palpites".format(cont))