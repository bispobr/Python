def leiadinheiro(msg):
    valido = False
    while not  valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro {entrada} preço invalido')
        else:
            valido = True
            return float(entrada)


def menu():
    print('--'*20 )
    print('MENU PRINCIPAL')
    print('--' * 20)
    print(' 1 - Ver Pessoas Cadastradas')
    print(' 2 - Cadastrar nova Pessoa')
    print('3 -  Saior do Sistema')
    print('--' * 20)
