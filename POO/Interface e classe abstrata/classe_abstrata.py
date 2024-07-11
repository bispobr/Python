from abc import ABC, abstractmethod, abstractproperty
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty    
    def marca(self):
        pass

class ControleTV(ControleRemoto):

    def ligar(self):
        print("LigandoTV...")
        print("Ligado")

    def desligar(self):
        print("DesligandoTV...")
        print("desligado")

    def marca(self):
        print("marca")


controle = ControleTV()
controle.ligar()
controle.desligar()
