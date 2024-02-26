valor = int(input())
ano = valor//365
valor= valor % 365
mes = valor //30
valor = valor % 30

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(valor))