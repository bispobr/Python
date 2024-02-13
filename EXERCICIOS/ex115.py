from utilidadescev import  dado

if dado.arquiexiste():
    dado.menu()
else:
    dado.criararquivo()
    dado.menu()




