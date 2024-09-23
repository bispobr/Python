import re
placas = [1,2,3,4,5,6,7,8,9,0]
dias = ["MONDAY","MONDAY", "TUESDAY","TUESDAY", "WEDNESDAY","WEDNESDAY", "THURSDAY" ,"THURSDAY" , "FRIDAY","FRIDAY"]
padrao = r'^[A-Z]{3}-[0-9]{4}$'
n = int(input())

for c in range(n):
    placa = str(input())
    match = re.match(padrao, placa)
    if match:
        print(dias[placas.index(int(placa[-1]))])
    else :
        print("FAILURE")