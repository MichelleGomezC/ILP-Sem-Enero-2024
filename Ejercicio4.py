# Ejercicio 4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

# Importar librerias o bibliotecas

# ENTRADA DE DATOS
# Declarar, crear o instanciar variables
grado_kelvin = float(input("Ingresa el grado kelvin: "))
grado_celsius = float(input("Ingresa el grado celsius: "))
grado_fahrenheit = float(input("Ingresa el grado fahrenheit: "))

# PROCESOS (Operaciones y/o calculos matemáticos y lógicos)
kelvin_a_celsius = grado_kelvin - 273.15
fahrenheit_a_celsius = (5 * (grado_fahrenheit - 32)) / 9
celsius_a_kelvin = grado_celsius + 273.15
kelvin_a_fahrenheit = ((9 * (grado_kelvin - 273.15)) / 5 ) + 32
fahrenheit_a_kelvin = ((5 * (grado_fahrenheit - 32)) / 9 ) + 273.15
celsius_a_fahrenheit = (9 * grado_celsius) / 5 + 32

# SALIDA DE DATOS
print("La conversión de kelvin a celsius es: ", kelvin_a_celsius)
print("La conversión de fahrenheit a celsius es:", fahrenheit_a_celsius)
print("La conversión de celsius a kelvin es: ", celsius_a_kelvin)
print("La conversión de kelvin a fahrenheit es: ", kelvin_a_fahrenheit)
print("La conversión de fahrenheit a kelvin es: ", fahrenheit_a_kelvin)
print("La conversión de celsius a fahrenheit es: ", celsius_a_fahrenheit)
