class animal:
    def __init__(self,qtdpatas,qtdolhos):
        self.qtdpatas = qtdpatas
        self.qtdolhos = qtdolhos

class mamifero (animal):
    def __init__(self, qtdpatas, qtdolhos):
        super().__init__(qtdpatas, qtdolhos)

class ave(animal):
    def __init__(self, qtdpatas, qtdolhos):
        super().__init__(qtdpatas, qtdolhos)

class cachorro(animal,mamifero):
    pass

class gato(animal,mamifero):
    pass

class leao(animal,mamifero):
    pass

class ornitorrinco(animal,ave):
    pass
    
