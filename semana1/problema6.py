"""
    Escriban una funcion la cual reciba un numero entero
    y retorne la suma de sus valores

    Ejemplo:

    2536 => 2 + 5 + 3 + 6 = 16
"""

def sum_digits(numero):
    total = 0
    for indice in numero:
        total += int(indice)
    return total

print(sum_digits(input("Ingrese un numero: ")))