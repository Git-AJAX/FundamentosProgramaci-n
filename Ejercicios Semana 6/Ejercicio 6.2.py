# EJERCICIO 6: OBTENER TODAS LAS CLAVES (KEYS) // MIÉRCOLES

# Agregar tu canción favorita
canción = {
    "título": "Her",
    "artista": "JVKE",
    "álbum": "Her",
    "año": 2025,
    "género": "Pop",
    "duración_segundos": 172
}

print("Diccionario de canción:")
print(canción)
print("\nTodas las claves del diccionario:")
claves = canción.keys()
print(claves)

print("\nMostrando claves una por una:")
for clave in claves:
    print("-", clave)