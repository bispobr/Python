a = float(input("Digite o tamanho da reta A:"))
b = float(input("Digite o tamanho da reta B:"))
c = float(input("Digite o tamanho da reta C:"))

if a < b + c and b < a + c and c < a + b:
    print("È possivel formar um triangulo!!!")
else:
    print("Não é possivel formar triangulo")