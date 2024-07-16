class Estudante:
    escola = "ABC"

    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero

    def __str__(self) :
        return f"{self.nome} - {self.numero} - {self.escola}"
    
def mostra(*objs):
    for obj in objs:
        print(obj)
    
ana = Estudante("ana clara",98521348)
bia = Estudante("Beatriz",587624685)

#mostra(ana)
#mostra(bia)

bia.numero = 55
Estudante.escola = "nova"
print(ana.__str__())
print(bia.__str__())