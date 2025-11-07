# EJERCICIO 3 // CONTAR VARIABLES
texto = "Alo, que haciendo mi gente en miercoles"
contador = 0
for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1
print(f"Hay {contador} vocales")