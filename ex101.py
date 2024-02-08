
def votar(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >=18 and idade <=100:
        msg = f'com {idade} :Voto obrigatorio'
    elif idade <16 or idade >100:
        msg = f'com {idade} :voto opcional'
    elif idade <16:
        msg = f'com {idade} :voto negado'
    return msg


nasc = int(input('Ano de nascimento:'))
print(votar(nasc))