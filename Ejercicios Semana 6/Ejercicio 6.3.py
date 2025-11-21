# EJERCICIO 6: VALIDAR EDAD PARA ENTRAR A UNA PELI // JUEVES

print("Ejercicio 6: Validar edad para entrar a una peli")
try:
    edad = int(input("¿Cuántos años tienes?: "))
    if edad < 0:
        print("ERROR: La edad no puede ser negativa")
    elif edad < 13:
        print("Puedes ver películas infantiles (G)")
    elif edad < 16:
        print("Puedes ver películas para adolescentes (PG-13)")
    elif edad < 18:
        print("Puedes ver películas de +15 (PG-15)")
    else:
        print("Puedes ver cualquier película, incluyendo mayores de 18")
except ValueError:
    print("ERROR: Debes escribir tu edad como número")