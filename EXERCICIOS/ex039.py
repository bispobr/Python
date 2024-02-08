from datetime import  date
nasc = int(input("Digite o ano de nascimento:"))
idade = date.today().year - nasc

if idade < 18:
    print("Não apto para o alistamento")
    print("ainda falta {} anos".format(18 - idade))
elif idade == 18:
    print("Apto para o alistamento!!!")
elif idade > 18:
    print("tempo de alistamento passado!!!")
    print("você esta {} anos atrasado".format(idade - 18))