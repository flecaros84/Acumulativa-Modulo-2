"""
Estimado/a estudiante,
Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
La empresa de catering "Gourmet Services" necesita desarrollar un sistema que permita gestionar los pedidos de sus clientes
para eventos corporativos y privados. Para el funcionamiento del sistema se requiere las siguientes funcionalidades:
Registrar Pedido: Para registrar un pedido se requiere lo siguiente: Nombre y apellido del cliente, número de contacto, detalles
del evento (tipo de evento, fecha y dirección), y menú seleccionado. Por ejemplo, la empresa ofrece menús de Comida Italiana,
Comida Japonesa, y BBQ. Debe permitir seleccionar entre una de las 3 opciones e ingresar la cantidad de comensales. Por lo
tanto, un detalle de pedido podría verse registrado de la siguiente maner:
Debe validar que todos los datos sean ingresados.
Listar Pedidos: Debe mostrar en la pantalla la lista de todos los pedidos realizados, similar al ejemplo anterior de registro de
pedidos.
Imprimir Detalle de Pedidos por Menú: Para imprimir el detalle de pedidos, el usuario debe seleccionar alguno de los menús
ofrecidos. Estos menús deben estar previamente definidos en algún tipo de colección de Python en el código, y por lo menos
deben ser tres, como los mencionados anteriormente. Al seleccionar uno de los menús se generarán 2 archivos de texto (.txt y un
.json) con el detalle de los pedidos que se han realizado con ese menú específico. Este debe tener la misma forma del registro
completo de las opciones anteriores pero en archivo de texto.
Salir del Programa: El programa debe funcionar hasta que el usuario decida salir.
GitHub: El código desarrollado por el estudiante debe ser subido en su plenitud a GitHub.
"""
import json

# Cargar archivo con registros
def Cargar_Archivo(archivo):
    try:
        with open(archivo, 'r') as leer:
            return json.load(leer)
    except FileNotFoundError:
        return []

def Guardar_Archivo(archivo, base_datos):
    with open(archivo, "w") as f:
        json.dump(base_datos, f, indent=4)

def ingresar_cliente():
    while True:
        cliente = input("Ingrese el nombre del cliente: ")
        if cliente != "":
            return cliente
        else:
            print("Nombre del cliente no puede ser vacio")

def ingresar_contacto():
    while True:
        try:
            contacto = int(input("Ingrese el N° de contacto: "))
        except ValueError:
            print("El número de contacto debe ser un entero de 9 digitos")
        else:
            celular = str(contacto)
            if celular.startswith("9") and len(celular)==9:
                return contacto
            else:
                print("Número de celular incorrecto. Debe iniciar con 9 tener 9 digitos")

def seleccionar_menu():
    while True:
        print("Menus Disponibles")
        print("1. Comida Italiana")
        print("2. Comida Japonesa")
        print("3. BBQ")
        try:
            opcion = int(input("Selecciona menu:"))
        except ValueError:
            print("Error. Debe seleccionar un entero entre 1 y 3")
        else:
            match opcion:
                case 1:
                    return "Comida Italiana"
                case 2:
                    return "Comida Japonesa"
                case 3:
                    return "BBQ"
                case _:
                    print("Error. Debe seleccionar un entero entre 1 y 3")

def ingresar_evento():
    while True:
        evento = input("Ingrese el tipo de evento: ")
        if evento != "":
            return evento
        else:
            print("Tipo de evento no puede ser vacio")    

def ingresar_comensales():
    while True:
        try:
            comensales = int(input("Ingrese el N° de comensales: "))
        except ValueError:
            print("Error. El número de comensales debe se un número entero")
        else:
            if comensales != None:
                return comensales
            else:
                print("Error. El número de comensales no puede ser nulo")

def registrar_pedido(base_datos):
    cliente = ingresar_cliente()
    contacto = ingresar_contacto()
    evento = ingresar_evento()
    menu = seleccionar_menu()
    comensales = ingresar_comensales()
    pedido = {
        "cliente": cliente,
        "contacto": contacto,
        "evento": evento,
        "menu": menu,
        "comensales": comensales
    }     
    base_datos.append(pedido)

def listar_pedidos(base_datos):
    for registro in base_datos:
        print(f"Cliente: {registro["cliente"]},Contacto: {registro["contacto"]},Evento: {registro["evento"]},Menú: {registro["menu"]},Comensales: {registro["comensales"]}\n")

# Imprimir detalle de pedidos de un determinado menu en txt
def ImprimirxMenu(base_datos):
    menu = seleccionar_menu()
    datos = []
    try:
        with open(f"{menu}.txt", "w") as f:
            for pedido in base_datos:
                if pedido["menu"] == menu:
                    f.write(f'{pedido["cliente"]},{pedido["contacto"]},{pedido["evento"]},{pedido["menu"]},{pedido["comensales"]} \n')
                    datos.append(pedido)
        ImprimirxMenuJSON(menu,datos)
    except FileNotFoundError:
        print("No se pudo crear el archivo")

def ImprimirxMenuJSON(menu,datos):
    with open(f"{menu}.json", 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f'Se ha creado el archivo {menu}')

def main():
    archivo = "pedidos.json"
    base_datos = Cargar_Archivo(archivo)
    while True:
        print("GOURMET SERVICES")
        print("Opciones del sistema:")
        print("1. Registrar pedido")
        print("2. Listar pedidos")
        print("3. Imprimir pedidos de un menu especifico")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese su selección: "))
        except ValueError:
            print("Opción invalida")
        else:
            match opcion:
                case 1:
                    registrar_pedido(base_datos)
                    Guardar_Archivo(archivo,base_datos)
                case 2:
                    listar_pedidos(base_datos)
                case 3:
                    ImprimirxMenu(base_datos)
                case 4:
                    break

if __name__ =="__main__": 
    main()