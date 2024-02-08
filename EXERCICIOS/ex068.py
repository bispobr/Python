from random import randint
venceu = True
v=0
while venceu:
    jn = int(input("Digite um valor:"))
    jop = str(input("Par ou Impar[Par/impar]")).strip().lower()
    pcn = randint(0,10)
    soma = jn + pcn
    if soma %2 == 0:
        rsoma = "par"
    else:
        rsoma = "impar"
    print("_______________________________________________")
    print(f'Você jogou {jn} e o computador {pcn}. total de {jn + pcn}  deu {rsoma}')
    print("_______________________________________________")
    if rsoma == jop:
        print("Voce Venceu!!!")
        print("Vamos Jogar Novamente....")
        v+=1
    else:
        print("Voce Perdeu")
        venceu = False
print(f"Game over! você venceu {v} vezes")
