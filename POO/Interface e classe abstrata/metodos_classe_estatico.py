class Pessoa:
    def __init__(self,nome = None,idade = None) :
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2024 - ano
        return cls(nome,idade)
    
    @staticmethod
    def maior_idade (idade):
        return idade >= 18
    


#p1 = Pessoa("ana",25)
#print(p1.nome,p1.idade)

p = Pessoa.criar_de_data_nascimento(2000,6,12,"bia")
print(Pessoa.maior_idade(15))
print(p.nome)

print(p.maior_idade(p.idade))
