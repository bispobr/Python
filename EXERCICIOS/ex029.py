vel = float(input("Qual a velocidade do Veiculo:"))
if vel > 80:
    dif = vel - 80
    multa = dif * 7
    print("Voce foi multado em R$ {:.2f}".format(multa))
else:
    print("Voce esta dentro do limite de velocidade!!!")