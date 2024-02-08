num = int(input("Digite um Valor:"))
base = int(input("qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal:"))
if base == 1:
    print("conversão binaria!!!")
    print("O valor {} convertido para binario {}".format(num,bin(num)[2:]))
elif base == 2:
    print("Base octal")
    print("o valoe {} convertido para octal {}".format(num,oct(num)[2:]))
elif base == 3:
    print("base hexadecimal")
    print("O valor {} convertido para hexadecimal {}".format(num,hex(num)[2:]))