carros = {'marca': 'fiat', 'modelo': 'uno', 'ano': 1997}
print(f'o carro {carros["modelo"]} foi fabricado em {carros["ano"]}')
print(carros.keys())
print(carros.values())
print(carros.items())
print('Monstrando só as keys')
for k in carros.keys():
    print(k)
print('Monstrando as keys e itens')
for k, c in carros.items():
    print(f'{k}:{c}')
del carros['ano']
print('=='*10)
for k, c in carros.items():
    print(f'{k}:{c}')
carros['modelo'] = 'palio'
print('=='*10)
for k, c in carros.items():
    print(f'{k}:{c}')
carros['motor'] = 2
print('=='*10)
for k, c in carros.items():
    print(f'{k}:{c}')
print("Didionario dentro de uma lista")
veiculos = []
carro1 = {'modelo':' gol','amo':1997}
carro2 = {'modelo' : 'palio', 'ano': 2010}
veiculos.append(carro1)
veiculos.append(carro2)
print(veiculos)