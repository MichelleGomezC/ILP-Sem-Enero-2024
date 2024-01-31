# Ejercicio 9. Realizar un Menú de Opciones y realizar una función para cada opción.

import random
import string

# Declarar o crear una función
def Lista(): 
    print("Lista de servicios de pasaje")
    return ["Uber", "Didi", "Metro"] 

def nómina():
    mes = input("Ingrese el mes: ")
    días_lab = int(input("Ingrese los días que laboró: "))
    pago_día = float(input("Ingrese el monto que se paga por día: "))
    pago_bruto = (pago_día * días_lab)
    iva_tras = (pago_bruto * .16)
    subtotal = (pago_bruto + iva_tras)
    iva_ret = (2/3 * iva_tras)
    isr_ret = (subtotal * .10)
    pago_neto = (subtotal - iva_ret - isr_ret)
    print("Calcular nómina de enero 2024", round(pago_neto, 2))
     
def generar_contraseña(longitud):
    if longitud > 5:
        print("Error: La longitud de la contraseña debe ser igual o menor a 5 caracteres.")
    else:
        contraseña = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))
        print("Contraseña generada:", contraseña)

def dat_personales():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su primer apellido: ")
    apellido2 = input("Ingrese su segundo apellido: ")
    edad = input("Ingrese su edad: ")
    print("Bienvenido ", nombre, apellido, apellido2)
    print("Nombre: ", nombre)
    print("Apellido paterno: ", apellido)
    print("Apellido materno: ", apellido2)
    print("Edad: ", edad)
    
# Mandar a llamar o invocar una función para ejecutarla
print("********** MENÚ **********")
print("1. Lista")
print("2. Nómina")
print("3. Generar contraseña")
print("4. Datos personales")
opción = int(input("Ingresa una opción: "))

if (opción == 1):
    Lista()
elif (opción == 2):
    nómina()
elif (opción == 3):
    generar_contraseña()
elif (opción == 4):
    dat_personales()

