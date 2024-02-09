def notas(*notas, sit = False):
    boletim = dict
    boletim = {'Total': len(notas), 'Maior': max(notas), 'menor': min(notas), 'media' : sum(notas)/len(notas)}
    if boletim['media'] > 7 :
        boletim['situação'] = 'boa'
    else:
        boletim['situação'] = 'Ruim'
    return boletim


print(notas(8,9,7,5))
