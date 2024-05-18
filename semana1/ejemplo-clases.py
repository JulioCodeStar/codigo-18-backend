# El nombre de la clase siempre debe empezar con mayúscula
class Persona:
    """
    Existe una función que se ejecuta cuando instanciamos a nuestra clase,
    a esa función se le dice constructor, podemos tener mas de 1 y la forma en
    la que se utiliza en python es con el nombre __init__
    """    

    """
    Cuando estamos dentro de una clase el primer parametro de TODAS las funciones
    sera self, luego de self podemos colocar los parametos que queramos
    """

    def __init__(self, nombre, apellido, edad, altura, direccion, peso):
        """
        Vamos a agregar propiedades a self y para hacer esto es de la siguiente
        manera

        self.nombre_de_la_propiedad = valor
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.direccion = direccion
        self.peso = peso

    def saludar(self):
        return f"Hola me llamo {self.nombre} {self.apellido} tengo {self.edad} años"
    
    def obtener_direccion(self):
        return f"Mi dirección del hogar es {self.direccion}"

"""
Para poder instanciar una clase, debemos simplemente llamarla por su nombre 
y guardarla en una variable
"""

persona1 = Persona("Julio", "Vargas", 22, 1.75, "Mz B", 85.3)

print(persona1.obtener_direccion())