# EJERCICIO 4 // ORDENAMOS PASO A PASO

numeros = [25, 18, 34, 79, 83]
print("Inicio:", numeros)
print("-" * 30)

n = len(numeros)

for i in range(n):
    print(f"\nPasada{i + 1}:")
    for j in range(0, n - i - 1):
        print(f"  Comparando {numeros[j]} y {numeros[j + 1]}")
        if numeros[j] > numeros[j + 1]:
            # Intercambiar
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            print(f"  Intercambio -> {numeros}")
        else:
            print(f"  No cambiar -> {numeros}")

print("\n" + "-" * 30)
print("Final:\n", numeros)        