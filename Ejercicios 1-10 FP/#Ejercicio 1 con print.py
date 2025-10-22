#Ejemplo 1 con print
print("Ejemplo 1\n")

#Instrucción 1
nombre = "Abi"

#Instrucción 2
edad = 17

#Instrucción 3
print("Hola, soy", nombre)

#Instrucción 4
print("Tengo", edad, "años")


#Ejemplo 2 con print
#2. Nueva Línea (\n)
print("\nEjemplo 2\n")

# Sin \n (todo en una línea)
print("Hola Mundo")
# Salida: Hola Mundo

#Con \n (salto de línea)
print("Hola\nMundo")

# Múltiples \n
print("Línea 1\nLínea 2\nLínea 3")


#Ejemplo 3 con tabulacion
print("\nEjemplo 3\n")

print("Nombre:\tEstefi")
print("Edad\t16")
print("Ciudad:\tMonterrey")


#Ejemplo 4 con tabulacion
print("\nEjemplo 4\n")

# Crear una conversación de chat
print("Ana:\tHola, ¿cómo estás?")
print("Luis:\tBien, ¿y tú?")
print("Ana:\t¡Genial!\n")
print("==== Chat guardado en ====")
print("C:\\Users\\Phython\\Documents\\chat.txt")

#Ejemplo 5
print("\nEjemplo 5\n")

# Dos argumentos
print("Hola","Mundo")
#Salida: Hola Mundo
#        ↑
#       espacio automático

# Tres argumentos
print("Me", "gusta", "dibujar")

# Mezclando tipos de datos
print("Tengo", 2, "mascotas en mi casa")

# Con variables
nombre = "Fer"
cantidad_hermanos = "1"
print("Me dicen", nombre, "y tengo", cantidad_hermanos, "hermana")


#Ejercicio 6. OPERADORES ARITMÉTICOS
print("\nEjercicio 6. OPERADORES ARITMÉTICOS\n")
# SUMA (+): vamos a sumar dos números
numero1 = 42
numero2 = 22
suma = numero1 + numero2
print("Operador suma:", suma)

# RESTA (-): ahora vamos a restar
resta = numero1 - numero2
print("Operador resta:", resta)

# MULTIPLICACIÓN (*): multiplicamos dos números
multiplicacion = numero1 * numero2
print("Operador multiplicación:", multiplicacion)

# DIVISIÓN (/): dividimos y obtenemos resultado con decimales 
division = numero1 / numero2
print("Operador división:", division)

#DIVISIÓN ENTERA (//): dividimos pero solo queremos la parte entera
division_entera = 10 // 3
print("Operador división entera:", division_entera)

# (%): obtiene el residuo (lo que sobra) de una división
residuo = 10 % 3
print("Operador residuo:", residuo)

#POTENCIA (**): elevar un número a una potencia
potencia = 2 ** 3
print("Operador potencial:", potencia)