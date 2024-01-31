# Ejercicio 7. Pedir el nivel del agua en metros de una cisterna

# ENTRADA DE DATOS
nivel_agua = int(input("Ingresa el nivel de agua: "))

# PROCESOS
if (nivel_agua > 6 ):
    print("Desbordamiento de agua en cisterna")
elif (nivel_agua == 6):
    print("Apagar bomba")
elif (nivel_agua >= 4  and nivel_agua <= 6):
    print("Desacelerar bomba")
elif (nivel_agua >= 2 and nivel_agua <= 4):
    print("La bomba está trabajando")
elif (nivel_agua > 0 and nivel_agua <= 2):
    print("Acelerar bomba de agua")
elif (nivel_agua == 0 ):
    print("Encender bomba de agua")
elif (nivel_agua < 0 ):
    print("Fuga en cisterna")
