class Conta:
    def __init__(self,agencia, saldo) :
        self._saldo = saldo
        self.agencia = agencia

    def depositar (self,valor):
        self._saldo += valor

    def sacar (self,valor):
        self._saldo -= valor;

    def saldo (self):
        print(self._saldo)

    def __str__(self) :
        return f"{self.__class__.__name__} : {[f"{chave} = {valor}" for chave,valor in self.__dict__.items()]}"
    

c1 = Conta(1550,500.95)
c1.depositar(100)
c1.sacar(50)
c1.saldo()
print(c1.__str__())    

  