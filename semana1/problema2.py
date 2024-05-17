# Escribir un programa si el cual me diga un numero es par o impar
try: 
    numero = int(input("Ingrese un numero: "))

    mensaje = "Es un numero impar"

    if numero % 2 == 0:
        mensaje = "Es un numero par"
    print(mensaje)
except Exception as e:
    print(f"Error: {e}")

