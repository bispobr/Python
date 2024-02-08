idadeM =tothomen=qtdMD= 0
continuar = "S"
while continuar == "S":
    idade=int(input("Digite a idade:"))
    sexo=str(input("Digite o sexo [M/F]")).strip().upper()[0]
    continuar = str(input("deseja Continuar [S/N]")).strip().upper()[0]
    if idade >=18:
        idadeM+=1
    if sexo == "M":
        tothomen+=1
    if sexo == "F" and idade < 20:
        qtdMD+=1

print(f"quantas pessoas tem mais de 18 anos :{idadeM}")
print(f"quantos homens foram cadastrados :{tothomen}")
print(f"quantas mulheres tem menos de 20 anos :{qtdMD}")

