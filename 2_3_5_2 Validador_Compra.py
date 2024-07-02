"""
2.3.5. Ejercicio 2 La empresa de ventas de productos tecnológicos “Chispa Divertida”, ha detectado
que en su página web de ventas se han generado reclamos por parte de los
clientes puesto que, al comprar productos, el sitio web no valida la información,
por tanto, los clientes pagan, pero la orden de compra no se procesa por falta de
datos.
Por lo tanto, la empresa le solicita a usted que antes de que se procese el pago, todos los campos sean validados.
En esta primera etapa, debe validar que los datos obligatorios existan.
El resultado debe visualizarse como aparece en la imagen.

"""
#Ingrese los siguientes datos para realizar su compra
#Todos los datos son obligatorios
#Nombre
#Teléfono
#Ingrese producto y cantidad
#Producto
#Cantidad
#¿Está seguro que desea pagar?
#('s' o 'n'):
#Faltan datos por ingresar. Por favor chequee la información ingresada

def funcion_telefono():
    while True:
        try:
            N_telefono = int(input("Teléfono: "))            
        except ValueError:
            print("Teléfono no válido")
        else:
            return N_telefono

def funcion_cantidad():
    while True:
        try:
            N_cantidad = int(input("Cantidad:"))
        except ValueError:
            print("Cantidad no válida")
        else:
            return N_cantidad

def funcion_checkout():
    while True:
        N_checkout = input("¿Está seguro que desea pagar?\n('s' o 'n'):").lower()
        if N_checkout == "s" or N_checkout == "n":
            return N_checkout
        else:
            print("Respuesta Incorrecta")

while True:
    print("Ingrese los siguientes datos para realizar su compra\nTodos los datos son obligatorios")
    nombre = input("Nombre: ")
    telefono = funcion_telefono()
    print("Ingrese producto y cantidad")
    producto = input("Producto: ")
    cantidad = funcion_cantidad()
    checkout = funcion_checkout()
    if checkout == 's':
        if nombre != "" and producto != "":
            print("Procesar pago")
            break
        else:
            print("\nFaltan datos por ingresar. Por favor chequee la información ingresada.")
            print("Nombre: ",nombre,"\nTeléfono: ",telefono,"\nProducto: ",producto,"\nCantidad: ",cantidad)
            print("\nVuelva a comenzar")
    else:
        print("Compra Cancelada")
        break
