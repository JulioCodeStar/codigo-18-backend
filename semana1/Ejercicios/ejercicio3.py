"""
    3. Contar ocurrencias de un elemento
       Escribe una función que reciba una lista y un elemento, y devuelva el número de veces que ese 
       elemento aparece en la lista.
"""

def contar_ocurrencias(lista, elemento):

    numeros_lista = lista.split(',')
    lista_final = []
    for n in numeros_lista:
        lista_final.append(int(n))

    # Utilizamos el método count() para contar las ocurrencias o coincidencias del elemento en la lista
    ocurrencias = lista_final.count(int(elemento))
    return ocurrencias

lista = input("Ingrese una lista separado por comas: ")
elemento = input("Ingrese el elemento a coincidir: ")

print(contar_ocurrencias(lista, elemento))