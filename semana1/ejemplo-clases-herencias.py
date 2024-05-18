class Persona:
    def __init__(self, nombre, apellido, edad=None, altura=None, peso=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
    def saludar(self):
        return f"Hola me llamo {self.nombre} {self.apellido}"



class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad_desde_Persona, carrera):
        super().__init__(nombre, apellido, edad=edad_desde_Persona)
        self.carrera = carrera

    def obtener_carrera(self):
        return f"Hola me llamo {self.nombre} y estudio {self.carrera}"


estudiante1 = Estudiante("Julio", "Vargas", 22
, "Ing Software")

print(estudiante1.saludar())
print(estudiante1.obtener_carrera())


# def crear_usuario(nombre, apellido, username, correo, password, direccion, pais, ciudad, dni):
#     return f"{nombre} {apellido} {correo} {password} {direccion} {pais} {ciudad} {dni}"


# crear_usuario("Pepe", "Perez", "pepe3hs", "pepe@gmail.com", "pepe123",
#               "av mi casa", "peru", "lima", "88888")

# crear_usuario("Lucho", "Perez", "lucho431", None,
#               "lucho123", None, "chile", None, None)


# def crear_usuario2(user):
#     return user


# # diccionario
# crear_usuario2({
#     "nombre": "Pepe",
#     "apellido": "Perez",
#     "username": "pepe3hs"
# })