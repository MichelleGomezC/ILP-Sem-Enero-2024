# FUNCIONES.- Son tareas a ejecutar o realizar
# SINTAXIS:
'''
def Nombre_de_la_función(parámetros o argumentos:)
| instrucciones o procesos que va a ejecutar la función
| return valor          (Se dice que devuelve, retorna o regresa un valor)
'''
# Declarar o crear una función
def Saludo():
    print("Hola Mundo")

def Suma(a, b):
    return a + b

def Restar(num1, num2):
    return num1 - num2
def Multiplicar(num1, num2):
    return num1 * num2
def Dividir(num1, num2):
    return num1 / num2

# Mandar a llamar o invocar una función para ejecutarla
print("********** MENÚ **********")
print("1. Saludo")
print("2. Suma")
print("3. Resta")
print("4. Multiplicación")
print("5. División")
respuesta = int(input("Ingresa una opción: "))

número1 = int(input("Ingresa un número: "))
número2 = int(input("Ingresa otro número: "))

if (respuesta == 1):
    Saludo()
elif (respuesta == 2):
    print("La suma =", Suma(número1, número2))     # Mando a llamar la función  y le paso o enviar los parámetros o argumentos
elif (respuesta == 3):
    print("La resta =", Restar(número1, número2))
elif (respuesta == 4):
    print("La multiplicación =", Multiplicar (número1, número2))
elif (respuesta == 5):
    print ("La división = ", Dividir (número1, número2))
else: 
    print("Opción no válida")


