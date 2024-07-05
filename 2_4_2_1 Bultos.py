"""2.4.2 Guía Ejercicios Ciclos o bucles
EJERCICIO 1
Realiza construcción de un programa que deba realizar lo siguiente:
Comienza con la inicialización de variables y solicita al usuario la cantidad de bul-
tos. Luego, utiliza un bucle FOR para procesar cada bulto, solicitando el peso al
usuario y manejando posibles errores (agregar excepciones). Dependiendo del
peso ingresado, acumula valores y contadores correspondientes para bultos livia-
nos y normales. Finalmente, imprime el total a pagar por bultos livianos y norma-
les, así como la cantidad de bultos en cada categoría
Una empresa de transporte requiere automatizar sus procesos de cálculo para po-
der cobrar por la cantidad de paquetes que trae un cliente.
Para calcular el valor total a cobrar y catalogarlo para envío, requiere preguntar el
peso de cada bulto y determinar el valor según lo siguiente:
Kilos Categoría Valor
1 - 5 Liviana $1,000
6 - 10 Normal $2,000
Ejemplo:
Si un cliente ingresa 3 bultos y según sus pesos estos clasifican en 1 liviano y 2
normales, el cliente debe paga $5,000
El sistema debe mostrar lo siguiente:
1 bulto liviano $1,000
2 bultos normales $4,000
Valor total a pagar: $5,000
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
for id_bulto in range (numero_bultos):
    peso_bulto = ingresar_peso(id_bulto)
    if clasificar_bulto(peso_bulto) == 0:
        livianos += 1
    elif clasificar_bulto(peso_bulto) == 1:
        normales += 1
print(f"{livianos} bulto(s) livianos ${livianos*1000:,}")
print(f"{normales} bulto(s) normales ${normales*2000:,}")
total_pagar = livianos*1000 + normales*2000
print(f"Valor total a pagar: ${total_pagar:,}")