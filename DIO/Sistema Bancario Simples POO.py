import textwrap
saldo = 0
limite = 500
extrato = ""
quantidade_saque = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

menu = """
==========================================
Banco Simples Digital
[c] criar usuario
[cc] criar conta
[l] listar contas
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

def criar_usuario(usuarios):
    cpf = int(input("cpf: (somente Numeros)"))
    usuario = usuario_filtro(cpf,usuarios)

    if usuario:
        print("Cpf já cadastrado não é possivel continuar a operação")
        return

    nome = str(input("Nome:"))
    data = str(input("Data de Nascimento:"))
    
    endereco = str(input("endereço:"))
    usuarios.append({"nome":nome,"data_nascimento":data,"cpf":cpf,"endereco":endereco})

    print ("Usuario criado com sucesso!!!")

def criar_conta(agencia,numero_conta,usuarios):
    cpf = int(input("cpf: (somente Numeros)")) 
    usuario = usuario_filtro(cpf,usuarios) 

    if usuario:
        print("Conta Criada")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("Usuario não encontrado, operação não pode ser concluida.")
  
def usuario_filtro(cpf,usuarios):
    filtro_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro_usuario[0] if filtro_usuario else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agencia:\t{conta['agencia']}
        c/c:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

while True:


    opcao = input(menu)

    if opcao == "c":
        print("Criação de usuario")
        criar_usuario(usuarios)

    elif opcao == "cc":
        print("criar conta")
        numero_conta= len(contas) + 1
        conta = criar_conta(AGENCIA,numero_conta,usuarios)

        if conta:
            contas.append(conta)
    elif opcao == "l":
        listar_contas (contas)

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

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao (self, conta, transacao):
        transacao.registrar (conta)

    def adicionar_Conta (self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self,nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        

class Conta:
    def __init__(self, numero, cliente) :
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n não a saldo suficiente!!!")
        elif valor >0:
            self._saldo -= valor
            print("\n operação realizda")
            return True
        else:
            print("\n operação falhou") 
        return False  
    
    def depositar (self, valor):
        if valor >0:
            self._saldo += valor
            print("\n operação bem sucedida")
        else:
            print("\n operação falhou")
            return False
        
        return True
    
    
class ContaCorrente (Conta):
    def __init__(self, numero, cliente,limite=500,limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar (self,valor):
        numero_saques = len(
            [Transacao for transacao in self.historico.trasacoes if transacao["tipo"]== Saque.__name__]
        )

        excedeu_limite =  valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n saque limite atingido.")
        elif excedeu_saques:
            print("\limite de saque atingido")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self) :
        return F"""\
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """
            

class Historico:
    pass

class Transacao(ABC):
    pass

class saque (Transacao):
    pass

class Deposito (Transacao):
    pass
    
