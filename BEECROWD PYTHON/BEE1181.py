m = [[],[],[],[],[],[],[],[],[],[],[],[]]

linha = int(input())
operacao = str(input())

for coluna in range(12):
    valor = float(input())
    m[linha][coluna] = valor
    soma += valor

if operacao == s:
    print("{:.1f}".format(soma))
elif operacao == m:
    print("{:.1f}".format(soma))