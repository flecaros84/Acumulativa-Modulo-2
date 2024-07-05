"""
2.5.4 Guía complementaria Ejercicios (Clase 14)
Ejercicio 2.
La empresa de comercializadora de confite, “Dulce Capricho” ha
creado un sitio web donde puede vender sus productos.
Como última etapa en la puesta en marcha del sitio, la empresa
desea que agregar 3 tipos de pago online para sus clientes. Estos
son:
 Tarjeta de crédito
 PayPal
 Transferencia electrónica
Si el pago es con tarjeta se deben solicitar:
 número de tarjeta de crédito
 Nombre del titular
 Mes de vencimiento
 Año de vencimiento
Si el pago es con PayPal debe ingresar:
 Nombre de usuario paypal
 Contraseña
Si el pago es por Transferencia electrónica:
 La empresa entrega sus datos para el pago
 Se indica un código de referencia
"""

def ingresar_tarjeta():
    while True:
        try:
            numero_tarjeta =int(input("Ingrese número de tarjeta: "))
            nombre_titular = input("Ingrese el nombre del titular: ")
            mes_vencimiento = int(input("Ingrese el mes de vencimiento (en número): "))
            year_vencimiento = int(input("Ingrese el año de vencimiento (en número): "))
            largo_n_tarjeta = len(str(numero_tarjeta))
        except ValueError:
            print("Datos erroneos")
        else:
            if mes_vencimiento == 0 or mes_vencimiento>12:
                print("El mes de vencimiento debe ser un número entre 1 y 12")
            elif year_vencimiento <= 2023:
                print("Tarjeta vencida")
            elif year_vencimiento > 2030:
                print("Año de vencimiento fuera de rango valido. Debe ser igual o menor a 2030")
            elif largo_n_tarjeta < 13 or largo_n_tarjeta > 18:
                print("Numero de tarjeta debe tener entre 13 y 18 digitos")
            else:
                print("Sus datos han sido ingresados correctamente")
                return

def paypal():
    while True:
        usuario_paypal = input("Ingrese su usuario Paypal: ")
        pass_paypal = input("Ingrese su password: ")
        if len(usuario_paypal) == 0 or len(usuario_paypal)>256:
            print("Error, usuario no tiene el largo requerido")
        elif len(pass_paypal) < 7 or len(pass_paypal) > 20:
            print("Error, el password no cumple con largo requerido")
        else:
            print("Sus datos han sido ingresados exitosamente y están siendo procesados")
            return
        
print("")
opcion = 0
pago = 100000
while True:
    print("***************Menu*******************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    print("")
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except:
        opcion = 0
    if opcion == 1:
        ingresar_tarjeta()
    elif opcion == 2:
        paypal()
    elif opcion == 3:
        print("Estos son los datos para la transferencia")
        print("Este es su código de transferencia")
    elif opcion == 4:
        print("Pago cancelado")
    elif opcion == 5:
        print("Hasta pronto...")
        break
    else:
        print("Opción no válida")
        print("")
        print("")
        print ("Muchas gracias por su compra")
        print("")