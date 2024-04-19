def recomendar_plano (consumo):
    resultado = ""
    if consumo<=10:
        resultado += f"Plano Essencial Fibra - 50Mbps"
    elif consumo >10 and consumo <=20:
        resultado += f"Plano Prata Fibra - 100Mbps"
    elif consumo > 20:
        resultado+= f"Plano Premium Fibra - 300Mbps"
    return resultado

consumo = float(input())
print(recomendar_plano(consumo))
