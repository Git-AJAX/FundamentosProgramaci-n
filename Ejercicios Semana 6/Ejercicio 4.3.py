# EJERCICIO 4: BUSCAR EN UN DICCIONARIO // JUEVES

print("Ejercicio 4: Buscar en un diccionario")
try:
    telefonos = {
        "Ethan": "555-1234",
        "Evan": "555-5678",
        "SHIZU": "555-9012"
    }

    nombre = input("¿De quién quieres el teléfono? ")
    telefono = telefonos[nombre]
    print(f"El teléfono de {nombre} es: {telefono}")
except KeyError:
    print("ERROR: Ese nombre no está en la agenda")