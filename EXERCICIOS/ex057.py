op=str(input("Informe o sexo [M/F]")).upper()
while op not in 'MF':
    op = str(input("Dado invalido!!!Informe o sexo [M/F]")).upper()
print("Sexo {} registrado com sucesso".format(op))