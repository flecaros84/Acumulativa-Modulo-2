"""
2.4.4 Actividad estructuras de decisión (Clase 11)
Deberás construir un programa que está diseñado para ayudar en la venta
de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
cada pasaje por separado. Si ingresas un valor que no es un número, te
indica que necesitas proporcionar un valor numérico válido. Al final, muestra
el monto total que se ha obtenido por la venta de todos los pasajes
 Solicita al usuario la cantidad de pasajes a vender.
 Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
 Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
acumula en la variable totalIngresos.
 Si el usuario ingresa un valor no numérico para el precio del pasaje,
el programa muestra un mensaje y sale del bucle usando break.
 Finalmente, se imprime el total de ingresos por la venta de pasajes
"""
def ingresar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese el n° de pasajes a vender: "))
        except ValueError:
            print("Debe ingresar un entero mayor a 0")
        else:
            if cantidad == 0:
                print("Debe ingresar un entero mayor a 0")
            else:
                return cantidad
            
cantidad = ingresar_cantidad()
totalIngresos = 0
for numero in range(cantidad):
    try:
        precio = int(input(f"Ingrese el precio del pasaje {numero}: "))
    except ValueError:
        print("Precio Incorrecto. Operación Abortada")
        break
    else:
        if precio == 0:
            print("Precio Incorrecto. Operación Abortada")
            break
        else:
            totalIngresos += precio 
print(f"El total de ingresos procesados fue de ${totalIngresos:,}")
