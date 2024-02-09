def menu ():
    print('===' * 20)
    print('sISTEMA DE AJUDA PYHELP')
    print('===' * 20)

while True:
    menu()
    resp = str(input('função ou programa:'))
    if resp == 'fim':
        break
    help(resp)