segundos = int(input())
hora = segundos// 3600
resto = segundos % 3600
minutos = resto // 60
resto = segundos %60
print('{}:{}:{}'.format(hora,minutos,resto))