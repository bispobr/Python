dia1,dia2,dia3 = [int (x) for x in str(input()).split()]

if (dia2 < dia1 and dia3 >= dia2):
    print(":)")
elif (dia2 > dia1 and dia3 <= dia2):
    print(":(")
elif (dia2 > dia1 and dia3 > dia2 and dia3 - dia2 < dia2 - dia1):
    print(":(")
elif (dia2 > dia1 and dia3 > dia2 and dia3 - dia2 >= dia2 - dia1):
    print(":)")
elif (dia2 < dia1 and dia3 < dia2 and dia2 - dia3 < dia1 - dia2):
    print(":)")
elif (dia2 < dia1 and dia3 < dia2 and dia2 - dia3 >= dia1 - dia2):
    print(":(")
elif (dia1 == dia2):
    if (dia3 > dia2):
        print(":)")
    else:
        print(":(")