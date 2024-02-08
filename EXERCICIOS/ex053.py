
frase = str(input("Frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for c in range(len(junto) - 1,-1,-1):
    inverso += junto[c]
if inverso == junto:
    print("Temos um palindromo")
else :
    print("A frase digitada não é um palindromo")

