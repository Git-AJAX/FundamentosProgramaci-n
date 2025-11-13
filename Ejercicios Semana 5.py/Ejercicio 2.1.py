# EJERCICIO 2: SUMA DE MATRICES 3x3

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Crear matriz resultado
resultado = []

# Sumar elemento por elemento
for i in range(3):  # 3 filas
    fila = []
    for j in range (3):  # 3 Columnas
        suma = matriz_a[i][j] + matriz_b[i][j]
        fila.append(suma)

    resultado.append(fila)
#Mostrar resultado
print("Resultado de la suma:")
for fila in resultado:
    for elemento in fila:
        print(elemento, end=" ")
    print()