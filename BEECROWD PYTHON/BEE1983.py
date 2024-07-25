alunos = int(input())

for c in range (alunos):
    matricula,nota = [float (x) for x in str(input()).split()]

    if c == 0:
        mnota = nota
        maluno = matricula
    elif nota > mnota:
        mnota = nota
        maluno = matricula


print(f'{maluno:.0f}' if mnota >=8 else "Minimum note not reached")