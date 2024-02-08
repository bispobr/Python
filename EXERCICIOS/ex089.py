alunos = list ()
lista = list()
while True:
    nome = str(input('nome do aluno:'))
    n1 =float(input('nota 1:'))
    n2 = float(input('nota 2:'))
    lista.append(nome)
    lista.append(n1)
    lista.append(n2)
    alunos.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar: [S/N]')).upper()
    if resp == 'N':
        break
print('============================')
for c in range (0,len(alunos)):
    print(f'Aluno {c} {alunos [c][0]} Media {((alunos[c][1]) + (alunos[c][2])) /2} ')
print('============================')
while True:
    pessoa = int(input('Mostrar nota de qual anuno?(999 interrompe)'))
    if pessoa == 999:
        break
    print(f'notas de {alunos[pessoa][0]} são {alunos[pessoa][1]} {alunos[pessoa][2]}')
    print('============================')
