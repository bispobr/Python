im = 0
sim = 0
sif = 0
idf = 0
totm = 0
totf = 0
nm = "p"
for c in range(1,5):
    nome = str(input("{} Nome:".format(c))).strip()
    idade = int(input("{} Idade:".format(c)))
    sexo = str(input("{} Sexo [m/F]:".format(c))).strip()
    if sexo == "m":
        totm +=1
        sim += idade
        if idade > im:
            im = idade
            nm = nome
    else:
        totf += 1
        sif += idade
        if idade < 20:
            idf += 1

print("Media de idade Grupo MASCULINO: {}".format(sim/totm))
print("O homem mais velho {} tem {} anos de idade".format(nm,im))
print("Media de idade do GRUPO FEMENINO: {}".format(sif/totf))
print("Mulheres idade menor que 20:{}".format(idf))