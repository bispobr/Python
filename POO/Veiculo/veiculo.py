class veiculo:
    def __init__(self,placa,ano,cor,marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.marca = marca

    def  ligar(self):
        print('Motor ligado')

    def desligar(self):
        print('desligar motor')

    def buzinar(self):
        print('buzinar')

    def __str__(self) :
        return f"{self.__class__.__name__} : {[f"{chave} = {valor}" for chave,valor in self.__dict__.items()]}"

class motocicleta(veiculo):
    def combustivel(self):
        print("etanol")

class carro (veiculo):
    def __init__(self, placa, ano, cor, marca,batido):
        super().__init__(placa, ano, cor, marca)
        self.batido = batido

    def avariado(self):
        print(F"{'SIM' if self.batido else 'nao'} bati o carro")

    
    
class caminhao (veiculo):
    pass



moto = motocicleta("JWE2584",2013,"AZUL","HONDA")
print(moto.__str__())
moto.ligar()
moto.combustivel()

carro0 = carro("asdw368",2074,"rosa","tigo",True)
carro0.desligar()
carro0.avariado()
print(carro0.__str__())

caminhao0 = caminhao("asdt2547",1984,"preto","ford")
print(caminhao0.__str__())
caminhao0.buzinar()