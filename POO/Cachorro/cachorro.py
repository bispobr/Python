class Cachorro:
    def __init__(self, nome, cor, acordado=True) :
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Latindo")

    def dormir(self):
        self.acordado = False
        print("zzzz....")


c1 = Cachorro("Dogo", "prata")
c2 = Cachorro("lara","caramelo", False )

c1.latir()
print(c1.nome)
c1.dormir()
print(c1.acordado)

c2.latir()
print(c2.acordado)