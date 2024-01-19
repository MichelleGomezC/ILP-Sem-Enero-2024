# Operaciones Matemáticas (Suma, Resta, Multiplicación, División, Potencia, Raíz Cuadrada, Modulo)

# Importar librerías de funciones matemáticas
import math 

# ENTRADA DE DATOS
número1 = float(input("Ingre7sa un número:")) # los input obtienen tipo de dato string
número2 = float(input("Ingresa otro número:"))

# PROCESOS (Operaciones y/o calculos matmáticos y lógicos)
suma = número1 + número2
resta = número1 - número2
multiplicación = número1 * número2
división = número1 / número2

potencia_1 = número1 ** número2 # 10 elevado a la potencia 5.7
potencia_2 = pow(número1, número2)
cuadrado = número1 ** 2
cubo = número2 ** 3

raíz_cuadrada_1 = math.sqrt(27)
raíz_cuadrada_2 = pow(27, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número1 % número2

# SALIDA DE DATOS
print("la suma es =", suma)
print("La resta es =", resta)
print("La multiplicación es =", multiplicación)
print("La división es =", división)
print("La división es =", round(división, 4))
print("La Potencia es =", potencia_1)
print("La potencia es =", potencia_2)
print("La potencia al cuadrado es =", cuadrado)
print("La potencia al cubo es =", cubo)
print("La raíz cuadrada es=", raíz_cuadrada_1)
print("La raíz cuadrada es =", raíz_cuadrada_2)
print("La raíz al cubo es =", raíz_cúbica)
print("El residuo es =", módulo_residuo)
