class bicicleta:
    def __init__(self,cor, modelo, ano, valor) :
        self.cor = cor
        self.modelo = modelo
        self.ano= ano
        self.valor = valor

    def buzinar (self):
        print("Bi BI")

    def parar (self):
        print("Parando")

    def correr (self):
        print("correndo")

    def __str__(self) :
        return f"{self.__class__.__name__} : {[f"{chave} = {valor}" for chave,valor in self.__dict__.items()]}"


b1 = bicicleta("amarela", "caloi",2010,2.500)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor)
print(b1.modelo)

print(b1.__str__())

