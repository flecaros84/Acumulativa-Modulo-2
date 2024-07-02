"""
Cálculo de Costo de Envío: Se le ha solicitado desarrollar un programa en Python para
calcular el costo de envío de paquetes para una empresa de logística. El programa debe
tener las siguientes funcionalidades:
1. Ingreso de datos del paquete:
    ○ El usuario ingresa el nombre del cliente, el peso del paquete en kilogramos y
    la distancia de envío en kilómetros.
    ○ Validar que el nombre del cliente no esté vacío y que tenga una longitud
    máxima de 30 caracteres.
    ○ Validar que el peso y la distancia sean valores numéricos positivos.
2. Cálculo del costo de envío:
    ○ El costo base de envío es de $5.000 CLP.
    ○ Por cada kilogramo de peso, se cobra un adicional de $500 CLP.
    ○ Si la distancia de envío supera los 100 kilómetros, se cobra un recargo de
    $100 CLP por cada kilómetro extra recorrido.
    ○ Calcular el costo total de envío sumando el costo base, el adicional por peso
    y el recargo por distancia.
3. Mostrar el costo de envío:
    ○ Mostrar un desglose del costo de envío, incluyendo el nombre del cliente, el
    peso del paquete, la distancia de envío, el costo base, el adicional por peso,
    el recargo por distancia (si corresponde) y el costo total de envío, todo
    ordenado y bien presentado.
4. Generar archivo de envío:
    ○ Crear un archivo de texto (.txt) con los datos del envío.
    ○ El archivo generado debe incluir el nombre del cliente, el peso del paquete, la
    distancia de envío y el costo total de envío, todo de forma ordenada y bien
    presentada.
    ○ El nombre del archivo generado debe seguir el formato
    "envio_[nombre_cliente].txt".
    Requerimientos técnicos:
    No olvides importar la librería “os” para trabajar creando archivos en el sistema operativo.
1- Utilizar funciones para modularizar el código (al menos una función para el cálculo
del costo de envío y otra para mostrar el desglose).
2- Utilizar variables para almacenar los datos ingresados y los resultados calculados.
3- Implementar estructuras condicionales para controlar el flujo del programa.
4- Implementar el manejo de errores con try except.
5- Utilizar estructuras de repetición para permitir el cálculo de múltiples envíos.
6- Subir el código fuente a tu repositorio en GitHub.
"""
global nombre_cliente
global peso_paquete
global distancia
global numero_paquetes
global ID_Paquete

def Ingreso_Cliente():
    while True:
        nombre_cliente = input("Ingrese nombre de cliente: ")
        if nombre_cliente == "":
            print("ERROR. El usuario no debe estar vacio")
        elif len(nombre_cliente) > 30:
            print("ERROR. El largo del nombre debe ser menor o igual a 30 caracteres")
        else:
            return nombre_cliente

def Ingreso_Paquetes():
    while True:
        try:
            numero_paquetes = int(input("Ingrese el N° de Paquetes a Ingresar: "))
        except ValueError:
            print("ERROR. Debe ingresar un entero positivo")
        else:
            if numero_paquetes <= 0:
                print("ERROR. Debe ingresar un entero positivo")
            else:
                return numero_paquetes

def Ingreso_Peso(ID_Paquete):
    while True:
        try:
            peso_paquete = float(input(f"Ingrese el peso del paquete N°{ID_Paquete} en kg: "))
        except ValueError:
            print("ERROR. Peso debe ser un número real positivo.")
        else:
            if peso_paquete <= 0:
                    print("ERROR. Peso debe ser un número real positivo")
            else:
                return peso_paquete

def Ingreso_Distancia(ID_Paquete):
    while True:
        try:
            distancia = float(input(f"Ingrese la distancia del paquete N°{ID_Paquete} en km: "))
        except ValueError:
            print("ERROR. Peso debe ser un número real positivo.")
        else:
            if distancia <= 0:
                print("ERROR. Peso debe ser un número real positivo")
            else:
                return distancia

nombre_cliente = Ingreso_Cliente()
numero_paquetes = Ingreso_Paquetes()
identificador = []
peso = []
distancia = []
costo_base = []
adicionalxpeso = []
recargoxdistancia = []
totalxpaquete = []
costo_base_total = 0
adicionalxpeso_total = 0
recargoxdistancia_total = 0
total = 0

for ID_Paquete in range (numero_paquetes):
    identificador.append(ID_Paquete)
    peso.append(Ingreso_Peso(ID_Paquete))
    distancia.append(Ingreso_Distancia(ID_Paquete))
    costo_base.append(5000)
    costo_base_total += costo_base[ID_Paquete]
    adicionalxpeso.append(round(peso[ID_Paquete]*500))
    adicionalxpeso_total += adicionalxpeso[ID_Paquete] 
    if distancia[ID_Paquete] > 100:
        recargoxdistancia.append(round((distancia[ID_Paquete] - 100) * 100))
    else:
        recargoxdistancia.append(0)
    recargoxdistancia_total += recargoxdistancia[ID_Paquete]
    totalxpaquete.append(costo_base[ID_Paquete]+adicionalxpeso[ID_Paquete]+recargoxdistancia[ID_Paquete])
    total += totalxpaquete[ID_Paquete]

identificador.append("Total")
costo_base.append(costo_base_total)
adicionalxpeso.append(adicionalxpeso_total)
recargoxdistancia.append(recargoxdistancia_total)
totalxpaquete.append(total)

print("RESUMEN DE SUS ENVIOS")
print(f"Nombre Cliente       :",nombre_cliente,sep ='\t')
print(f"N° de Paquetes       :",numero_paquetes,sep ='\t')
print(f"ID Paquetes          :",*identificador, sep ='\t')
print(f"Peso (kg)            :",*peso, sep ='\t')
print(f"Distancia (km)       :",*distancia, sep ='\t')
for i in range(len(costo_base)):
    costo_base[i] = f"{costo_base[i]:,}"
print(f"Costo Base x Paquete :",*costo_base, sep ='\t')
for i in range(len(adicionalxpeso)):
    adicionalxpeso[i] = f"{adicionalxpeso[i]:,}"
print(f"Costo Adic x Peso    :",*adicionalxpeso, sep ='\t')
for i in range(len(recargoxdistancia)):
    recargoxdistancia[i] = f"{recargoxdistancia[i]:,}"
print(f"Costo Adic x Distanc :",*recargoxdistancia,sep ='\t' )
for i in range(len(totalxpaquete)):
    totalxpaquete[i] = f"{totalxpaquete[i]:,}"
print(f"Total                :",*totalxpaquete,sep ='\t' )

while True:
    try:
        archivo = open(f"envio_{nombre_cliente}.txt","r")
        archivo = open(f"envio_{nombre_cliente}.txt","w")
        archivo.write("RESUMEN DE SUS ENVIOS\n")
        archivo.write(f"Nombre Cliente       :\t{nombre_cliente}\n")
        archivo.write(f"N° de Paquetes       :\t{numero_paquetes}\n")
        archivo.write(f"ID Paquetes          :\t{'\t'.join(map(str, identificador))}\n")
        archivo.write(f"Peso (kg)            :\t{'\t'.join(map(str, peso))}\n")
        archivo.write(f"Distancia (km)       :\t{'\t'.join(map(str, distancia))}\n")
        archivo.write(f"Costo Base x Paquete :\t{'\t'.join(map(str, costo_base))}\n")
        archivo.write(f"Costo Adic x Peso    :\t{'\t'.join(map(str, adicionalxpeso))}\n")
        archivo.write(f"Costo Adic x Distanc :\t{'\t'.join(map(str, recargoxdistancia))}\n")
        archivo.write(f"Total                :\t{'\t'.join(map(str, totalxpaquete))}\n")
        print(f"Se ha escrito el archivo envio_{nombre_cliente}.txt")
        break
    except FileNotFoundError:
        print("El archivo no existe. Creando informe_ventas.txt")
        archivo = open(f"envio_{nombre_cliente}.txt", "x")