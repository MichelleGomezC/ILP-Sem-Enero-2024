# Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE

número = int(input("Ingrese el número: "))

if (número > -100 and número < 0):
    for i in range(-1, -101, -2):
        print("", i)
        # print("Es válido")

if (número > 0 and número < 100):
    for i in range(2, 99, 2):
        print("", i)

elif (número == 0 or número <= -100 or número >= 100):
        print("Es inválido")




