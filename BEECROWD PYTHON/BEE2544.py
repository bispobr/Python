import math
while True:
    try:
        ninjas = int(input())
        print(int(math.log(ninjas, 2)))  
    except EOFError:
        break