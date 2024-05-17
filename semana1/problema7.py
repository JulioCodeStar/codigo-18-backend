"""
    Escribe una función contar_palabras que reciba una cadena
    y devuelva el número de palabras que contiene

    hola como estas
    3
"""

def contar_palabras(frase):
    # conteo = frase.split(" ")
    # total = len(conteo)
    # return total

    return len(frase.split(" "))

frase = input("Ingrese una frase: ")

print(contar_palabras(frase))