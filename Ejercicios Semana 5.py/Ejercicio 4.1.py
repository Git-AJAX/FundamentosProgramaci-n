# EJERCICIO 4: ENCUENTRA EL ELEMENTO MAYOR

matriz = [
    [15, 8],
    [23, 12]
]
# Empezamos asumiendo que el primero es el mayor
mayor = matriz[0][0]  # Empieza con el 15
# Recorremos toda la matriz
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:  # Si encuentro uno más grande
            mayor = elemento  # Lo guardo como el nuevo mayor

# Mostramos resultado 
print("La matriz es:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
print(f"\nEl número mayor es: {mayor}")