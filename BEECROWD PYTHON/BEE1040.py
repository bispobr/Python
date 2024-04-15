valores = str(input()).split()
n1 = float(valores[0])
n2 = float(valores[1])
n3 = float(valores[2])
n4 = float(valores[3])
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1 )/(2 + 3 + 4 + 1)

print("Media: {:.1f}".format(media))
if (media >= 7):
    print("Aluno aprovado.")
elif (media < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    n5 = float(input().strip())
    print("Nota do exame: {:.1f}".format(n5))
    mediaFinal = (media + n5) / 2


    if (mediaFinal >= 5.0):
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mediaFinal))
    else :
        print(" Aluno reprovado.")
        print("Media final: {:.1f}".format(mediaFinal))