#Ejercicio 10. OPERADORES DE IDENTIDAD
print("Ejercico 10. Operadores de identidad\n")

# Programa que compara objetos 
print("=== ¿SON LA MISMA COSA? ===") 
#Creamos dos listas que se ven iguales
lista1 = ["manzana", "pera"] 
lista2 = ["manzana", "pera"] 
lista3 = lista1   # lista3 es la MISMA que lista1 

# IS (es): Pregunta: ¿Son el mismo objeto en la memoria?
print("¿lista1 es lista2? (is):", lista1 is lista2)    # False (diferentes objetos)
print("¿lista1 es lista3? (is):", lista1 is lista3)    # True (mismo objeto)

# IS NOT (no es): Pregunta: ¿NO son el mismo objeto?
print("lista1 NO es lista2? (is not):", lista1 is not lista2)   # True