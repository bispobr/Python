renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen" , "Rudolph"]
bolas = sum([int (x) for x in input().split()])

while True:
    
    if bolas == 0:
        break
    
    for c in range (len(renas)):
        bolas -=1

        if bolas == 0:
            print(f'{renas[c]}')
            break