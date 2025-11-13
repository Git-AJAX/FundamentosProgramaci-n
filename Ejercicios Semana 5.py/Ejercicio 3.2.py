# EJERCICIO 3 // ORDENAR CALIFICACIONES

calificaciones = [85, 92, 78, 100, 88, 70]
print("Calificaciones desordenadas:\n", calificaciones)

n = len(calificaciones)

for i in range(n):
    for j in range(0, n - i - 1):
        if calificaciones[j] > calificaciones[j + 1]:
            calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]

print("Calificaiones ordenadas:\n", calificaciones)
print("Calificación más baja:\n", calificaciones[0])
print("Calificación más alta:\n", calificaciones[-1])