# Ejercicio 8. Calcular la nómina para un empleado en el mes de Mayo del 2023 conociendo su pago por día de 250 pesos 

# ENTRADA DE DATOS
mes = input("Ingrese el mes: ")
días_lab = int(input("Ingrese los días que laboró: "))
pago_día = float(input("Ingrese el monto que se paga por día: "))

# PROCESOS 
pago_bruto = (pago_día * días_lab)
iva_tras = (pago_bruto * .16)
subtotal = (pago_bruto + iva_tras)
iva_ret = (2/3 * iva_tras)
isr_ret = (subtotal * .10)
pago_neto = (subtotal - iva_ret - isr_ret)

# SALIDA DE DATOS
print("El pago neto del mes es: ", round(pago_neto))



