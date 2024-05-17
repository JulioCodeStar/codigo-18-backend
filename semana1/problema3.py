"""
Escribe un programa que calcule el área de un círculo dado su radio
(Área = pi * radio**2).
Pide el radio del usuario
"""

import math

try: 
    radio = float(input("Ingrese el valor del radio: "))
    area = math.pi * (radio**2)
    print(f"El área del circulo es: {area}")
except Exception as e:
    print(f"Error: {e}")