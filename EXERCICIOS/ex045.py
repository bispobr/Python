# CORIIGIR REGRAS DO JOGO
import random
itens = ('Pedra', 'papel','TESOURA')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
op = int(input('Qual é a sua escolha: '))
oppc = random.randint(0,2)
print('o computador escolheu {}'.format(itens[oppc]))
print('o Jogador escolheu   {}'.format(itens[op]))

if oppc == 0:
    if op == 0:
        print('empate!!!')
    elif op == 1:
        print('Derrota!!! Computador venceu!!!')
    else:
        print('Vitoria!!! JOGADOR VENCEU!!!')
elif oppc == 1:
    if op == 0:
        print('Vitoria!!! JOGADOR VENCEU!!!')
    elif op == 1:
        print('empate!!!')
    else:
        print('Derrota!!! Computador venceu!!!')
elif oppc == 2:
    if op == 0:
        print('Vitoria!!! JOGADOR VENCEU!!!')
    elif op == 1:
        print('Derrota!!! Computador venceu!!!')
    else:
        print('empate!!!')