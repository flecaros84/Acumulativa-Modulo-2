"""
Guia 2.3.5. Ejercicio 5
La pizzeria Cesar’s Pizza, contiene una variada gama de pizzas para
escoger. La pizzeria se caracteriza por tener una atención rápida y
mantener sus precios más bajos que la competencia.
La gerencia le solicita realizar un programa que permita calcular los
costos del pedido con sus respectivos valores del neto, impuesto y total.
El algoritmo es el siguiente. Una vez que usted lo terminó, se da cuenta
que podría mejorar el código de la asignación de los valores de las
pizzas, puesto que hay varias pizzas con el mismo precio.
"""
#Agregue un validador a la opción
def ingresar_opcion():
    while True:
        try: 
            opcion = int(input("Elija su pizza. Ingrese el número de la pizza deseada:"))
        except ValueError:
            print("Debe ingresar un entero entre 1 y 10")
        else:
            if opcion==0 or opcion>10:
                print("Debe ingresar un entero entre 1 y 10")
            else:
                return opcion

def ingresar_cantidad():
    while True:
        try: 
            cantidad = int(input("¿Cuantas pizzas desea?: "))
        except ValueError:
            print("Debe ingresar un entero mayor a 0")
        else:
            if cantidad==0:
                print("Debe ingresar un entero mayor a 0")
            else:
                return cantidad

print("")
print("Bienvenido a Cesar's Pizza")
print("Menu:")
print("1.- PEPPERONI")
print("2.- QUESO")
print("3.- JAMÓN")
print("4.- 4N1")
print("5.- HULA HAWAIIAN")
print("6.- ULTIMATE SUPREME")
print("7.- VEGGIE")
print("8.- 3 MEAT TREAT")
print("9.- SUPER CHEESE 4N1")
print("10.- CHICKEN BBQ")
print("")
opcion = ingresar_opcion()
cantidad = ingresar_cantidad()
if opcion == 1:
    precio = 6000
elif opcion == 2:
    precio = 7000
elif opcion == 3:
    precio = 8000
elif opcion == 4 or opcion ==5:
    precio = 10000
elif opcion == 6:
    precio = 11000
elif opcion <= 7:
    precio = 12000
neto = precio * cantidad
iva = neto * 0.19
total = neto + iva
print(f"El neto de su pedido es {neto}")
print(f"El impuesto de su pedido es {iva}")
print(f"El total as pagar es {total}")


