class animal:
    def __init__(self,qtdpatas,qtdolhos):
        self.qtdpatas = qtdpatas
        self.qtdolhos = qtdolhos

    def __str__(self) :
        return f"{self.__class__.__name__} : {[f"{chave} = {valor}" for chave,valor in self.__dict__.items()]}"

class mamifero (animal):
    def __init__(self, cor,**kw):
        super().__init__(**kw)
        self.cor = cor

class ave(animal):
    def __init__(self, asas,**kw):
        super().__init__(**kw)
        self.asas = asas

#class cachorro(mamifero):
#    pass

#class gato(mamifero):
#    pass

class leao(mamifero):
    pass

class ornitorrinco(mamifero,ave):
    def __init__(self, cor, **kw):
        super().__init__(cor, **kw)
    

leao0= leao(qtdpatas=4,qtdolhos=2,cor="verde")
print(leao0.__str__())

orn = ornitorrinco(qtdpatas=4,qtdolhos=2,cor="preto",asas = 2)
print(orn.__str__())