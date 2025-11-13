# EJERCICIO 5 // ORDEN DESCENDENTE

numeros = [51, 23, 85, 17, 19]
print("Original:\n", numeros)
n = len(numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        # CAMBIO: < en lugar de >
        if numeros[j] < numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Ordenado (mayor a menor):\n", numeros)