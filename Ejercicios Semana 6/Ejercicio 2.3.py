# EJERCICIO 2: DIVISIÓN ENTRE NÚMEROS // JUEVES

print("Ejercicio 2: División entre números\n")

try:
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))
    resultado = numero1 / numero2
    print(f"El resultado de {numero1} / {numero2} = {resultado}")
except ZeroDivisionError:
    print("ERROR: No puedes dividir entre cero")
except ValueError:
    print("Error: Debes escribir números, no texto")