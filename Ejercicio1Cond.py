# Ejercicio 1

# APROBADO               Rango entre >6 y 10
# APENAS APROBADO        Equivalente a 6 
# REPROBADO              Rango entre 0 y < 6
# PROMEDIO NO VÁLIDO     Menor que 0 o mayor que 10 

# ENTRADA DE DATOS 
calificación_1 = float(input("Ingresa tu calificación: "))
calificación_2 = float(input("Ingresa tu calificación: "))
calificación_3 = float(input("Ingresa tu calificación: "))

# PROCESOS 

promedio = (calificación_1 + calificación_2 + calificación_3) / 3

print("El promedio es: ", promedio)

if (promedio > 6 and promedio <= 10):
    print("APROBADO")
elif (promedio == 6 ):
    print("APENAS APROBADO")
elif (promedio >= 0 and promedio < 6 ):
    print("REPROBADO")
elif (promedio < 0 or promedio > 10):
    print("PROMEDIO NO VÁLIDO")
6