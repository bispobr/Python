casos = int(input())

for c in range (casos):
    x,y = [int (x) for x in input().split()]
    op = x + y

    match(op):
        case 0:
            print("PROXYCITY")
        case 1:
            print("P.Y.N.G.")
        case 2:
            print("DNSUEY!")
        case 3:
            print("SERVERS")
        case 4:
            print("HOST!")
        case 5:
            print("CRIPTONIZE")
        case 6:
            print("OFFLINE DAY")
        case 7:
            print("SALT")
        case 8:
            print("ANSWER!")
        case 9:
            print("RAR?")
        case 10:
            print("WIFI ANTENNAS")