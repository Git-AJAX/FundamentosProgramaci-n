# EJERCICIO 3 // SEMANA 4 // SUMA ACUMULATIVA
print("\nEJERCICIO 3 CON WHILE - SUMA ACUMULATIVA")

# Inicializamos las variables
numeros = 1
suma = 0

#Mientras numeros sea menor o igual a 50
while numeros <= 50:
    suma = suma + numeros    # Acumulamos la suma
    numeros = numeros + 1    # Incrementamos el contador 

print(f"La suma del 1 al 50 es: {suma}\n")