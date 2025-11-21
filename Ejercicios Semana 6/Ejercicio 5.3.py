# EJERCICIO 5: MULTIPLICAR NÚMERO POR TEXTO // JUEVES

print("Ejercicio 5: Multiplicar número por texto")
try:
    numero = int(input("¿Cuántas veces quieres ver el mensaje?: "))
    mensaje = input("¿Cuál es el mensaje?: ")
    print(mensaje * numero)
except ValueError:
    print("ERROR: Debes escribir un número entero")
except TypeError:
    print("ERROR: No se puede hacer esa operación")