"""
    2. Calcular el promedio de una lista
    Escribe una función que reciba una lista de números y devuelva el promedio de esos números.
"""

def promedio_lista(numeros):
    numeros_list = numeros.split(",")
    numeros_int = []
    for n in numeros_list:
        numeros_int.append(int(n))

    # La funcion sum hace la suma de una lista con la condición que sean numeros
    suma = sum(numeros_int)

    # Para contar la cantidad en la lista
    cantidad = len(numeros_int)
    
    promedio = suma / cantidad

    return promedio


numeros = input("Ingrese los numeros separados por comas: ")

promedio = promedio_lista(numeros)

print(f"El promedio final de la lista de números es: {promedio}")
