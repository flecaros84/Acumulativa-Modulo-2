#Diccionarios de Producto y Precio
Producto = {
            1: "Pan ciabatta",
            2: "Pie de limón",    
            3: "Café",
            4: "Té",
            5: "Alfajor"
            }
Precio =   {
            1: 2000,
            2: 3500,
            3: 2200,
            4: 1600,
            5: 1000
            }
Cantidad =  {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
            }
Venta =     {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
            }

#Función para Ingresar cantidad vendida de cada producto
def Ingreso_Ventas(posicion_id):
    while True:
        print("Ingrese cantidad vendida de",Producto[posicion_id])
        try:
            cantidad_ingresada = int(input("Cantidad Vendida = "))
        except ValueError: 
            print("Debe ingresar un número entero")
        else:
            return cantidad_ingresada

#Algoritmo principal, recorre diccionarios y utiliza la función de Ingreso_Ventas para registrar cantidades
#Luego multiplica precio x cantidad de cada producto para obtener su venta
print("Ingreso de Ventas\n_________________\nProducto / Precio:")
Venta_Total = 0
for posicion in Producto:
    print(Producto[posicion],"/",Precio[posicion])
    Cantidad[posicion] = Ingreso_Ventas(posicion)
    Venta[posicion] = Precio[posicion]*Cantidad[posicion]
    Venta_Total +=Venta[posicion]
#Imprime en pantalla el resumen de ventas del dia
print("Producto / Precio / Cantidad / Venta" )
for posicion in Producto:
    print(f"{Producto[posicion]} / {Precio[posicion]} / {Cantidad[posicion]} / {Venta[posicion]}")
#Escribe un archivo con el informe de ventas
while True:
    try:
        archivo = open("informe_ventas.txt","r")
        archivo = open("informe_ventas.txt","w")
        archivo.write("Producto / Precio / Cantidad / Venta\n")
        for posicion in Producto:
            archivo.write(f"{Producto[posicion]} / {Precio[posicion]} / {Cantidad[posicion]} / {Venta[posicion]}\n")
        print("Se ha generado el archivo informe_ventas.txt")
        break
    except FileNotFoundError:
        print("El archivo no existe. Creando informe_ventas.txt")
        archivo = open("informe_ventas.txt", "x")