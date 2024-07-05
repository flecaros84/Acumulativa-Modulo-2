"""2.4.2 Guía Ejercicios Ciclos o bucles
EJERCICIO 2
Ahora, realiza la siguiente modificación al programa anterior:
• El bucle For, debe ser reemplazado por una sentencia While, que permita
ejecutarse mientras la variable “nroBulto” sea menor o igual a la cantidad de
bultos ingresados por el usuario.
• Recuerda incluir sentencias de validación.
"""

#Función para ingresar el N° de bultos
def ingresar_numero_bultos():
    while True:
        try:
            numero_bultos = int(input("Ingrese el N° de bultos: "))
        except ValueError:
            print("Debe ingresar un número entero mayor a 0")
        else:
            if (numero_bultos == 0):
                print("Debe ingresar un número entero mayor a 0")
            else:
                return numero_bultos

#Función para ingresar el peso de cada bulto
def ingresar_peso(id_bulto):
    while True:
        try:
            peso_bulto = int(input(f"Ingrese el peso del bulto N°{id_bulto} en kg: "))
        except ValueError:
                print("Debe ingresar un número real entre 1 y 10")
        else:
            if (peso_bulto < 1 or peso_bulto > 10):
                print("Debe ingresar un número real entre 1 y 10")
            else:
                return peso_bulto

#Función para clasificar el peso de cada bulto
def clasificar_bulto(peso_bulto):
    if peso_bulto <= 5:
        return 0
    else:
        return 1

livianos = 0
normales = 0
numero_bultos = ingresar_numero_bultos()
nroBulto = 1
while nroBulto <= numero_bultos:
    peso_bulto = ingresar_peso(nroBulto)
    if clasificar_bulto(peso_bulto) == 0:
        livianos += 1
    elif clasificar_bulto(peso_bulto) == 1:
        normales += 1
    nroBulto +=1
print(f"{livianos} bulto(s) livianos ${livianos*1000:,}")
print(f"{normales} bulto(s) normales ${normales*2000:,}")
total_pagar = livianos*1000 + normales*2000
print(f"Valor total a pagar: ${total_pagar:,}")