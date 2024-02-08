from datetime import datetime
pessoa = dict()

pessoa["nome"] = str(input('Qual o seu nome :'))
nasc = int(input('Ano de nascimento:'))
pessoa['idade'] = datetime.now().year - nasc
pessoa ['ctps'] = int(input('Carteira de Trabalho (0 não tem:)'))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação:'))
    pessoa['salario'] = float(input('Salario : R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - nasc

print('==='*10)
for a,b in pessoa.items():
    print(f'{a} tem o valor {b}')
