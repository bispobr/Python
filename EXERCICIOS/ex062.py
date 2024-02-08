PrimeiroTermo1 = int(input("Primeiro termo:"))
razao = int(input("Razão da PA:"))
inicio=1
fim=10
mais = 1
while mais !=0:
    while inicio <= fim:
        print(PrimeiroTermo1, end=">")
        PrimeiroTermo1+=razao
        inicio+=1
        mais=int(input("Quantos termos voce quer mostrar a mais:"))
        fim = mais
print("fim")

print("Tentar fazer depos!!!!")