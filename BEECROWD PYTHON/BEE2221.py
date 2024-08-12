t = int(input())
for c in range(t):

    bonus = int(input())
    atq1, def1, level1 = [int(x) for x in input().strip().split(' ')]
    valorGolpe1 = (atq1 + def1) /2

    atq2, def2, level2 = [int(x) for x in input().strip().split(' ')]
    valorGolpe2 = (atq2 + def2) /2

    if level1 % 2 == 0:
        valorGolpe1 += bonus

    if level2 % 2 == 0:
        valorGolpe2 += bonus


    if valorGolpe1 > valorGolpe2 :
        print('Dabriel')
    elif valorGolpe2 > valorGolpe1 :
        print('Guarte')
    else:
        print('Empate')