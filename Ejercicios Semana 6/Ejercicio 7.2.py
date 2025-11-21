# EJERCICIO 7: OBTENER TODOS LOS VALORES (VALUES) // MIÉRCOLES

calificaciones = {
    "Economía": 8.5,
    "Derecho de aduanas": 9.0,
    "Admin de negocio": 8.0,
    "Logística y cadena de suministro": 7.5,
    "Mercadottecnia Internacional": 9.5
}

print("Diccionario de calificaciones:")
print(calificaciones)
print("\nTodos los valores del diccionario:")
valores = calificaciones.values()
print(valores)

print("\nMostrando valores uno por uno:")
for valor in valores:
    print("-", valor)
print("\nPromedio de calificaciones:", sum(valores) / len(valores))