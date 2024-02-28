import math

#DECLARANDO VARIABLES

g = float(input("Ingrese el valor de la constante g:\n"))

r = float(input("Ingrese el valor de radio en kilometros: \n"))

# SOLUCION DEL PROBLEMA

Ve = math.sqrt(2*g*r*1000)

# MOSTRANDO EL RESULTADO

print(f"La velocidad de Escape es: {Ve:.1f}[m/s]")

