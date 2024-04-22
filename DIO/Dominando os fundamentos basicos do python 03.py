import re

def validade_numero_telefonr(phone_number):
    pattern = r'^\([0-9]{2}\) [0-9]?[0-9]{4}-[0-9]{4}$'
    if re.match(pattern,phone_number):
        resultado = f"Número de telefone válido."
    else:
        resultado = f"Número de telefone inválido."
    return resultado

numero = input()
result = validade_numero_telefonr(numero)
print(result)

