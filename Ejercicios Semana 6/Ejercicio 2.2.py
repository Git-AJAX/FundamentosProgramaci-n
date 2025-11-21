# EJERCICIO 2: AGREGAR UN NUEVO PAR CLAVE-VALOR // MIÉRCOLES

videojuego = {
    "título": "Minecraft",
    "plataforma": "PC"
}

print("Diccionario original:")
print(videojuego)
# Agregar nuevos datos
videojuego["año"] = 2011
videojuego["género"] = "Sandbox"
videojuego["es_multijugador"] = True

print("\nDiccionario después de agregar datos:")
print(videojuego)
print("\nNuevos datos agregados:")
print("Año:", videojuego["año"])
print("Género:", videojuego["género"])
print("¿Es multijugador?:", videojuego["es_multijugador"])