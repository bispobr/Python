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
    print(' 3 -  Saior do Sistema')
    print('--' * 20)
    leiaop('Sua Opção:')


def leiaop(msg):
    ok = False
    cont = 0
    while not ok:
        try:
            cont += 1
            n = int(input(msg))
            if n >=1 and n <=3:
                ok = True
                switch_case(n)
            else:
                print('Erro! Digite uma opção entre 1 e 3 ')

        except:
            print('Erro! Digite um numero valido')
            if cont >=2:
               menu()


def switch_case(x):
    match x:
        case 1:
            print('++'*20)
            print('opção 1')
            print('++' * 20)
            menu()
        case 2:
            print('++' * 20)
            print('opção 2')
            print('++' * 20)
            menu()

        case 3:
            print('++' * 20)
            print('Saindo do Sistema')
            print('++' * 20)


