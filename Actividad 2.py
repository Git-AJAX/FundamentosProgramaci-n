# ACTIVIDAD 2 CANVAS
print("=== PRECIOS DE BOLETOS ===")

# Precios a pagar 
menores_tres_años = 0
menor_edad = 30
mayor_de_18 = 45 

# Descuentos
descuento_mayor_de_edad = 12
descuento_docente = 10
descuento_estudiante = 10

# Pedir los datos 
edad = int(input("Edad del visitante:   "))
if edad <= 3:
    print("El visitante no paga boleto")
else:
    if edad < 18:
        precio_base = 30
    else:
        precio_base = 45

print("1. Visitante mayor de edad\n")
print("2. Visitante estudiante\n")
print("3. Visitante docente\n")
print("4. Visitante regular\n")
tipo = int(input("\n Tipo de visitante:   "))


