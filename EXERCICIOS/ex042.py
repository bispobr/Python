a = float(input("Digite o tamanho da reta A:"))
b = float(input("Digite o tamanho da reta B:"))
c = float(input("Digite o tamanho da reta C:"))

if a < b + c and b < a + c and c < a + b:
    print("È possivel formar um triangulo!!!")
    if a == b == c:
        print("Tipo do triangulo : triangulo equilatero")
    elif a != b != c != a:
        print("Tipo do triangulo : triangulo escaleno")
    else:
        print("Tipo do triangulo : triangulo isoceles")

else:
    print("Não é possivel formar triangulo")

