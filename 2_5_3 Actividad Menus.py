"""
2.5.3 Actividad Menús (Clase 13)
El programa debe tener un menú de opciones de donde se pueda realizar el pago
del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
una vez sumadas se resten al cupo disponible.
Las opciones disponibles deben estar construidas de la siguiente forma:
1. Pago de Tarjeta de Crédito:
a. El usuario comienza con una deuda de $100.000
b. El usuario puede ingresar un monto para realizar un pago en la
tarjeta de crédito.
c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
d. Se debe verificar que el monto a pagar no exceda el saldo actual de
la tarjeta.
e. Al pagar el sistema debe descontar de la deuda total
f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
saldo de la tarjeta.
2. Simulación de Compras:
a. El usuario puede simular realizar un número ilimitado de compras.
b. Para cada compra, se solicita al usuario ingresar el monto de la
compra. El programa suma los montos de cada compra.
c. Se verifica que el monto de la compra sea mayor o igual a cero.
d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
iteración del bucle for.
3. Salir:
a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
A considerar:
1. Manejo de Errores:
a. Se utilizan bloques try y except para manejar posibles errores al
ingresar datos, validar valores no numéricos y errores inesperados.
2
b. Se debe programar mensajes de error específicos para guiar al
usuario sobre posibles problemas.
"""

def pago(deuda):
    print(f"Deuda Actual {deuda:,}")
    try:
        pago = int(input("Ingrese el monto de pago: "))
    except ValueError:
        print(f"El monto a pagar debe ser un entero mayor a 0 y menor o igual a {deuda:,}")
        return deuda
    else:
        if pago==0 or pago > deuda:
            print(f"El monto a pagar debe ser un entero mayor a 0 y menor o igual a {deuda:,}")
            return deuda
        else:
            print(f"Pago exitoso por {pago:,}")
            return deuda-pago            

def numero_compras():
    while True:
        try:
            numero_compras = int(input("Ingrese el n° de compras: "))
        except ValueError:
            print("El n° de compras debe ser un entero mayor a 0")
        else:
            if numero_compras == 0:
                  print("El n° de compras debe ser un entero mayor a 0")
            else:
                return numero_compras

def realizar_compras(numero_compras, deuda):
    for compra in range(numero_compras):
        while True:
            try:
                monto_compra = int(input(f"Ingrese el monto de compra N°{compra+1}: "))
            except ValueError:
                print("El monto de la compra debe ser un entero mayor a 0")
            else:
                if monto_compra == 0:
                    print("El monto de la compra debe ser un entero mayor a 0")
                else:
                    deuda += monto_compra
                    break
    return deuda

deuda = 100000
while True:
    print("Menú:")
    print(f"Su deuda actual es: {deuda:,}")
    print("1. Pago de Tarjeta de Crédito.")
    print("2. Simulación de Compras.")
    print("3. Salir.")
    try:
        opcion = int(input(f"Ingrese su opción: "))
    except ValueError:
        print("Debe elegir una opción entre 1 y 3")
    else:
        if opcion == 0 or opcion >3:
            print("Debe elegir una opción entre 1 y 3")
        elif opcion == 1:
            deuda = pago(deuda)
        elif opcion == 2:
            n_compras = numero_compras()
            deuda = realizar_compras(n_compras,deuda)
        elif opcion == 3:
            print("Gracias por operar con nosotros")
            break