# EJERCICIO 4: ELIMINAR UN PAR CLAVE-VALOR // MIÉRCOLES

# Escribe tus datos
cuenta = {
    "usuario": "Shun",
    "email": "Hayakunaruu_07@gmail.com", 
    "teléfono": "81 3666 7150",
    "ciudad": "Michigan"
}

print("Cuenta original (con teléfono):")
print(cuenta)
# Eliminar el número de teléfono por pivacidad
del cuenta["teléfono"]

print("\nCuenta después de eliminar teléfono:")
print(cuenta)
print("\nVerificación - ¿existe 'teléfono'?:", "teléfono" in cuenta)