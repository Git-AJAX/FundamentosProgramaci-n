# EJERCICIO 1: SUMA DE MATRICES 2x2

# Paso 1: Crear las dos matríces
matriz_a = [
    [1, 2],
    [3,4]
]
matriz_b = [
    [5,6],
    [7,8]
]
# Paso 2: Crear matriz vacía para el resultado
resultado = []
# Paso 3: Recorrer las matrices y sumar
for i in range(2):  # 2 filas
    fila = [] # Crear fila vacía

    for j in range(2):   # 2 Columnas
        suma = matriz_a[i][j] + matriz_b[i][j]  # Sumar elementos
        fila.append(suma)  # Agregar a la fila

    resultado.append(fila)  # Agregar fila al resultado

# Paso 4: Mostrar resultado
print("Matriz A:")
for fila in matriz_a:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\nMatriz B:")
for fila in matriz_b:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\nResultado A + B")
for fila in resultado:
    for elemento in fila:
        print(elemento, end=" ")
    print()