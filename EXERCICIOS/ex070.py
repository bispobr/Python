tot =p1000= 0
Pmenor = 1000000
continuar = "S"
while continuar == "S":
    nome = str(input("Nome do produto:"))
    preco=float(input("Preço do produto:"))
    tot+=preco
    if preco > 1000:
        p1000+=1
    if preco <Pmenor:
        Pmenor = preco
        mproduto = nome
    continuar = str(input("deseja Continuar [S/N]")).strip().upper()[0]

print(f"qual é o total gasto na compra:{tot}")
print(f"quantos produtos custam mais de R$1000:{p1000}")
print(f"qual é o nome do produto mais barato :{mproduto} custando {Pmenor}")