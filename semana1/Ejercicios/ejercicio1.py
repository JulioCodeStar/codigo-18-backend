"""
    1. Ordenar una lista
    Escribe una función que reciba una lista de números y devuelva una nueva lista con los elementos 
    ordenados de manera ascendente.
"""

def order_number(numeros):
    # Convertimos la cadena de texto a una lista de numeros usando el bucle for
    numeros_list = numeros.split(',')
    numeros_int = []
    for n in numeros_list:
        numeros_int.append(int(n))

    # la función sorted ordena una lista
    lista = sorted(numeros_int)
    return lista

numeros = input("Ingrese una lista de numeros separados por la ,: ")


print(order_number(numeros))