# ARREGLOS / LISTAS.- Variable que almacena una colección de datos.
# SINTAXIS:
'''
nombre_de_la_variable = [valor1, valor2, valor3, ...]
A los valores de la colección también se llaman elementos
'''

# Declarar o crear una lista
nombres = ["Michelle", "Hugo", "Aarón", "Ignacio"]
# índice: 0      1       2        3      index
edades = [20, 30, 40, 50]

# OPERACIONES CON ARREGLOS / LISTAS
# Agregar o insertar un elemento al final de la lista
nombres.append("Eduardo")
edades.append(60)

# Eliminar un elemento de una lista 
nombres.remove("Hugo")
edades.remove(30)

#Acceder y editar a un elemento de una lista
nombres[0] = "Miguel"
edades[0] = 25

#Obtener la longitud de una lista
print(len(nombres))  #lenght
print(len(edades))

# Ordenar una lista
nombres.sort()
edades.sort(reverse=True)

print("NOMBRE: ", nombres)
print("EDADES: ", edades)


