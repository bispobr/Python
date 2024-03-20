dia1 = int(input().split()[1])
hr1, min1, seg1 = map(int, input().split(':'))
tempo1 = seg1 + min1*60 + hr1*60*60 + dia1 *24*60*60

dia2 = int(input().split()[1])
hr2, min2, seg2 = map(int, input().split(':'))
tempo2 = seg2 + min2*60 + hr2*60*60 + dia2*24*60*60

tempo = tempo2 - tempo1
dias = tempo//(24*60*60)

tempo = tempo % (24 * 60 * 60)

horas = tempo // (60 * 60)

tempo = tempo % (60 * 60)

minutos = tempo // 60

segundos = tempo % 60

print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")