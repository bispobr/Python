from random import randint
escolha = int(input("Em que numero eu pensei?"))
pc = randint(0,5)
if escolha == pc:
    print("Parabens!!! Voce Acertou")
else:
    print("Voce errou o palpite, eu pensei no numero {}".format(pc))