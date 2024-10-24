while True:
    try:
        n = int(input())
        livros=[]

        for c in range(n):
            livros.append(str(input()))
  
        livros.sort()

        for livro in livros:
            print(livro)
            
        livros.clear()
    except EOFError:
        break