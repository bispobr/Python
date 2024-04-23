saldo = 0
limite = 500
extrato = ""
quantidade_saque = 0
LIMITE_SAQUES = 3

menu = """
==========================================
Banco Simples Digital
[c] criar usuario
[cc] criar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================================
=> """
def saque(*,valor,limite,saldo,quantidade_saque,LIMITE_SAQUES,extrato):
    if valor > limite:
        print(f"O valor de R$ {valor} excede o limite de R$ 500 por saque.")
    elif valor > saldo:
        print(f"o valor de R$ {valor} excede o saldo Disponivel.")
    elif quantidade_saque >= LIMITE_SAQUES:
        print(f"Quantidade de saque Diario Excedida.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        quantidade_saque += 1
        print(f"saque de R$ {valor} Realizado")
    else:
        print("Operação falhou!")
    return saldo, extrato, quantidade_saque

def deposito(deposito,saldo,extrato,/,):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Operação Aprovada!Valor Depositado.")
    return saldo, extrato

def extra(saldo,/,*,extrato):
    print("==========================================")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "c":
        print("Criação de usuario")

    elif opcao == "cc":
        print("criar conta")

    elif opcao == "d":
      try:
        depositar = float(input("valor a ser depósito: "))
        saldo, extrato = deposito(depositar,saldo,extrato)

      except ValueError:
          print("Digige um numero! tente Novamente")

    elif opcao == "s":
      try:
        valor = float(input("valor do saque: "))
        saldo,extrato,quantidade_saque = saque(valor = valor,limite=limite,saldo=saldo,LIMITE_SAQUES=LIMITE_SAQUES,extrato=extrato,quantidade_saque=quantidade_saque)

      except ValueError:
          print("Digige um numero! tente Novamente")

    elif opcao == "e":
       extra(saldo,extrato=extrato)

    elif opcao == "q":
        print("==========================================")
        print("saindo do Banco Digial Simples ")
        print("==========================================")
        break

    else:
        print("Opção invalida!.")