# EJERCICIO 4 // ENCONTRAR EL NÚMERO MAYOR
print("\n EJERCICIO 4")

numeros = [15, 42, 8, 23, 67, 31]
mayor = numeros[0]   # Empezamos con el primero de la lista
for num in numeros:
    if num > mayor:
        mayor = num
print(f"El número mayor es: {mayor}")