class TabelaHash:
    def __init__(self, M):
        self.M = M
        self.tabela = [[] for _ in range(self.M)]

    def funcaoHash(self, valor):
        return valor % self.M

    def adiciona(self, valor):
        self.tabela[self.funcaoHash(valor)].append(str(valor))

    def imprime(self):
        for i in range(self.M):
            if(len(self.tabela[i]) > 0):
                lista = ' -> '.join(self.tabela[i])
                print(f'{i} -> {lista} -> \\')
            else:
                print(f'{i} -> \\')


N = int(input())

for i in range(N):
    if(i):
        print('')

    M, C = [int(x) for x in input().strip().split(' ')]
    numeros = [int(x) for x in input().strip().split(' ')]

    tabelaHash = TabelaHash(M)
    for numero in numeros:
        tabelaHash.adiciona(numero)
    tabelaHash.imprime()