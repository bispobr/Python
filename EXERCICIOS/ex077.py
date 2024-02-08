frase = ("uma","coisa","que","eu","quero","phython")
for palavra in frase:
    print(f"na palavra {palavra.upper()} temos: ")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra)