aluno = dict()
aluno['nome'] = input('Nome do aluno :')
aluno['nota'] = int(input('nota do aluno :'))
if aluno['nota'] > 6:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprevado'
print(f'Nome do aluno {aluno["nome"]}')
print(f'nota do aluno {aluno["nota"]}')
print(f'situação do aluno {aluno["situação"]}')
