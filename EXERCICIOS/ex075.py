num = (int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')))
print(f'valores digitados {num}')
print("Quantas vezes apareceu o valor 9: {}".format(num.count(9)))
if 3 in num:
    print("Em que posição foi digitado o primeiro valor 3: {}".format(num.index(3)))
else:
    print("o valor 3 não está presente em num")
for c in num:
    if c%2 == 0:
        print(f'numero PAR {c}')
