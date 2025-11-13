# EJERCICIO 6 // PROMEDIO DE CALIFICACIONES

def calcular_promedio(cal1, cal2, cal3):
    suma = cal1 + cal2 + cal3
    promedio = suma / 3
    return promedio

promedio = calcular_promedio(85, 90, 78)
print(f"Tu promedio es: {promedio}")

promedio2 = calcular_promedio(100, 95, 88)
print(f"Tu promedio es: {promedio2}")