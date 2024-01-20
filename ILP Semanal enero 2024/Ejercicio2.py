# Ejercicio 2. Calcular el área y perímetro de un círculo.

# Importar librerias o bibliotecas

# ENTRADA DE DATOS
# Declarar, crear o instanciar variables
radio = float(input("Ingresa el radio: "))

PI = 3.1416 

# PROCESOS (Operaciones y/o calculos matemáticos y lógicos)
perímetro = 2 * PI * radio
área = PI * (radio ** 2)  

# SALIDA DE DATOS
print("El perimetro es = ", perímetro)
print("El área es = ", área)
