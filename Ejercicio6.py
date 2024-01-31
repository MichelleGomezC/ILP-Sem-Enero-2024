# Ejercicio 6. Pedir un número y decir si es par o impar

# ENTRADA DE DATOS
número = int(input("Ingresa un número: "))

# PROCESOS 
if número % 2 == 0:
    print(f"{número} es un número par.")
elif número % 2 != 0:
    print(f"{número} es un número impar.")


