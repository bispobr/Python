try:       
    while True: 
        n = int(input())

        if n % 2:
            pass               

        for i in range(1,n + 1, 2):
            vazio = (n - i) // 2 
            print(' ' * vazio + '*' * i)

        for i in range(1, 4, 2):
            vazio = (n - i) // 2 
            print(' ' * vazio + '*' * i)        
        
        print()
except EOFError:
    pass