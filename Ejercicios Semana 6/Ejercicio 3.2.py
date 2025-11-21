# EJERCICIO 3: MODIFICAR UN VALOR EXISTENTE // MIÉRCOLES

# Agregar tus datos 
perfil = {
    "usuario": "Shun",
    "Seguidores": 500,
    "publicaciones": 25,
    "ciudad": "Michigan"
}

print("Perfil original:")
print(perfil)
print("Seguidores antes:", perfil["Seguidores"])
# Modificar valores (gana más seguidores)
perfil["Seguidores"] = 1250
perfil["publicaciones"] = 45

print("\nPerfil actualizado:")
print(perfil)
print("Seguidores ahora:", perfil["Seguidores"])
print("Publicaciones ahora:"), perfil["publicaciones"]