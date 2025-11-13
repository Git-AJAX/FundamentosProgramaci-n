# EJERCICIO 1 // TU PRIMERA LISTA ORDENADA

numeros_lista = [5, 2, 8, 1, 9, 12, 4]
print("Lista original:", numeros_lista)

# Ordenar con Bubble Sort
n = len(numeros_lista)  # n = 7 elementos en numeros_lista

for i in range(n):
    for j in range(0, n - i - 1):
        # Comparar vecinos
        if numeros_lista[j] > numeros_lista[j + 1]:
            # Intercambiar
            numeros_lista[j], numeros_lista[j + 1] = numeros_lista[j + 1], numeros_lista[j]
print("Lista ordenada:", numeros_lista)