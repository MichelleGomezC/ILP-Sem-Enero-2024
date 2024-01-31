# MAYOR O MENOR DE EDAD

# ENTRADA DE DATOS
# Declarar o crear variables y constantes
edad = int(input("Ingresa tu edad: "))

# PROCESOS (Operacionesy/o cálculos matemáticos)
if (edad >= 18 and edad <= 120):                      # Rango de valores aceptados: (18 - 120) 
    print("Es MAYOR DE EDAD")             
elif (edad >= 0 and edad < 18):                     # Rango de valores aceptados: (0 - < 18)
    print("Es MENOR DE EDAD")
elif (edad < 0 or edad > 120):                      # else: # Valores no válidos (<0 , > 120)   
    print("Edad no válida")
else:                                 # Valores no válidos: (< 0 , > 120)
    print("Edad no válida")




