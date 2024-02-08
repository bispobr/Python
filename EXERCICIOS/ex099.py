def maior (*num):
    print('***' * 20)
    print('Analiasndo os valores...')
    print(f'{num} foram informados {len(num)} valores ao todo')
    print(f'o maior valor informado foi {max(num)}')
    print('***' * 20)


maior(1,5,7,9,3,6,8,7)
maior(1,8,6,8)
maior(1,2)
