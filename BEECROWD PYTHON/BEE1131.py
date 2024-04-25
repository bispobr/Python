novo_Grenal = qtd_vitoria_gremio= qtd_vitoria_inter= empates = grenais = 0
while novo_Grenal != 2:
    inter, gremio = [int (x) for x in str(input()).split()]
    grenais +=1
    if inter > gremio:
        qtd_vitoria_inter+=1
    elif gremio > inter:
        qtd_vitoria_gremio+=1
    elif gremio == inter:
        empates+=1
    if qtd_vitoria_gremio > qtd_vitoria_inter:
        venceu_mais_grenais = "Gremio"
    else:
        venceu_mais_grenais = "Inter"

    print("Novo grenal (1-sim 2-nao)")
    novo_Grenal = int(input())

print(f"{grenais} grenais")
print(f"Inter:{qtd_vitoria_inter}")
print(f"Gremio:{qtd_vitoria_gremio}")
print(f"Empates:{empates}")
print(f"{venceu_mais_grenais} venceu mais")