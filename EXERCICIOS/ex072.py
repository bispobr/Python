numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
num = int(input('Digite um numero entre 0 e 10:'))
while not (num >= 0 and num <= 10):
    num = int(input('tente novamente.Digite um numero entre 0 e 10:'))
print(f'você digitou o numero {numeros[num]}')