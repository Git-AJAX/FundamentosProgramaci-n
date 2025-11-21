# EJERCICIO 3: ACCEDER A ELEMENTOS DE UNA LISTA // JUEVES

print("Ejercicio 3: Acceder a elementos de una lista")
try:
    amigos = ["Juan", "María", "Carlos", "Sofia"]
    posicion = int(input("¿Cuál es el número de amigo que quieres ver? (1-4): "))
    # Restamos 1 porque las listas empiezan en 0
    amigo = amigos[posicion - 1]
    print(f"Tu amigo es: {amigo}")
except IndexError:
    print("ERROR: Ese número no existe en la lista")
except ValueError:
    print("ERROR: Debes escribir un número") 