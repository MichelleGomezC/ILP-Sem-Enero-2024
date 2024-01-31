# Ejercicio 12. Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos insertados uno por uno y ordenados de forma ascendente.


def ingresar_y_ordenar_números():
    lista_numérica = []

    # Insertar elementos uno por uno
    for i in range(1, 11):
        número = int(input(f"Ingrese el número {i}: "))
        lista_numérica.append(número)

    # Ordenar la lista de forma ascendente
    lista_numérica.sort()

    # Mostrar la lista ordenada

    print("Lista numérica ordenada de forma ascendente: ", lista_numérica)

# Llamar a la función
ingresar_y_ordenar_números()

