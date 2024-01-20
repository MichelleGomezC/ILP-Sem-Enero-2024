# Ejercicio 5. Obtener valores para: a, b y c. Calcular la fórmula general.

# Importar librerias o bibliotecas
import math

# ENTRADA DE DATOS
# Declarar, crear o instanciar variables
valor_a = float(input("Ingrese el valor a: "))
valor_b = float(input("Ingrese el valor b: "))
valor_c = float(input("Ingrese el valor c: "))

# PROCESOS (Operaciones y/o calculos matemáticos y lógicos)
fórmula1 = (- valor_b - math.sqrt(valor_b ** 2 - 4 * valor_a * valor_c)) / (2 * valor_a)
fórmula2 = (- valor_b + math.sqrt(valor_b ** 2 - 4 * valor_a * valor_c)) / (2 * valor_a)

#SALIDA DE DATOS
print("El resultado de la f1 es: ", fórmula1)
print("El resultado de la f2 es: ", fórmula2)

