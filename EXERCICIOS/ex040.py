n1 = int(input("Digite a nota 1 :"))
n2 = int(input("Digite a nota 2 :"))
media = (n1 + n2) / 2

if media < 5 :
    print("Media {}".format(media))
    print("Reprovado")
elif media >=5 and media <= 6.9 :
    print("Media {}".format(media))
    print("Recuperação")
elif media >= 7:
    print("Media {}".format(media))
    print("Aprovado!!!!")