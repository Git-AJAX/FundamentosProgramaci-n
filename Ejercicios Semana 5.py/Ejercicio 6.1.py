# EJERCICIO 6 // DESAFÍO

numeros = [12, 5, 9, 2, 15]
print("Original:\n", numeros)
n = len(numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] ___ numeros[j + 1]:   # ¿Qué va aquí?
            numeros[j], numeros[j + 1] = ___ , ___ # Completa

print("Ordenado:\n", numeros)