edad = int(input(" Ingresa tu edad:  "))
genero = input("Ingresa tu género favorito (acción, comedia, terror):  ").lower()

if edad < 13:
    print(" Te recomendamos películas infantiles... ")

elif edad >= 13 and edad <= 17 and genero == "acción":
    print("Te recomendamos: Spider-Man (PG-13)")

elif edad >= 13 and edad <= 17 and genero == "comedia":
    print("Te recomendamos: Shrek (PG-13)")

elif edad >= 13 and edad <= 17 and genero == "terror":
    print("Te recomendamos: Scary Stories4 (PG-13)")

elif edad >= 18 and genero == "acción":
    print("Te recomendamos: John Wick")

elif edad >= 18 and genero == "comedia":
    print("Te recomendamos: Superbad)")

elif edad >= 18 and genero == "terror":
    print("Te recomendamos: El Conjuro")