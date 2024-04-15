menu = """
==========================================
Banco Simples Digital

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================================
=> """

saldo = 0
limite = 500
extrato = ""
quantidade_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
      try:
        deposito = float(input("valor a ser depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Operação Aprovada!Valor Depositado.")
      except ValueError:
          print("Digige um numero! tente Novamente")

    elif opcao == "s":
      try:
        valor = float(input("valor do saque: "))

        if valor > limite:
            print(f"O valor de R$ {valor} excede o limite de R$ 500 por saque.")
        elif valor > saldo:
            print(f"o valor de R$ {valor} excede o saldo Disponivel.")
        elif quantidade_saque > LIMITE_SAQUES:
            print(f"Quantidade de saque Diario Excedida.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saque += 1
            print(f"saque de R$ {valor} Realizado" )
        else:
            print("Operação falhou!")
      except ValueError:
          print("Digige um numero! tente Novamente")

    elif opcao == "e":
        print("==========================================")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("==========================================")
        print("saindo do Banco Digial Simples ")
        print("==========================================")
        break

    else:
        print("Opção invalida!.")