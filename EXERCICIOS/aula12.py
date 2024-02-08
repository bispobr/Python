nome = str(input("Qual é o seu nome?"))
if nome == 'bruno':
        print("belo nome!!!")
elif nome == 'pedro' or nome == 'joao':
    print("nome popular!!!")
elif nome in 'ana maria julia gabriela':
    print('Belo nome femenino')
else:
    print("Seu nome é comun!!!")
print("Prazer em te conhecer {}".format(nome))