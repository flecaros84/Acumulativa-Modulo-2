"""
El almacén, “Diego’s” en su afán de incorporar nuevas tecnologías en
sus procesos de negocio, le solicita un prototipo de sistema que le
permita ingresar los datos de 3 ventas del almacén.
Antes de usted, el almacén le había pedido a un informático comenzara hacer el sistema, pero este lo dejó botado.
Ahora los dueños desean que usted siga con el desarrollo.
¿Cuál sería el algoritmo que permite obtener el siguiente resultado (de la imagen)?
"""
print("Ingresar los datos de la venta")
cliente = input("Ingrese el nombre del cliente: ")
precio1 = int(input("Ingrese el precio del producto1: "))
cantidad1 = int(input("Ingrese la cantidad del producto1: "))
precio2 = int(input("Ingrese el precio del producto2: "))
cantidad2 = int(input("Ingrese la cantidad del producto2: "))
precio3 = int(input("Ingrese el precio del producto3: "))
cantidad3 = int(input("Ingrese la cantidad del producto3: "))
descuento = int(input("Ingrese el decuento: "))
total_bruto = (precio1 * cantidad1) + (precio2 * cantidad2) + (precio2 *cantidad2)
precio_con_descuento = round(total_bruto - (total_bruto *descuento/100))
iva = round(0.19*precio_con_descuento)
print("")
print(f"Cliente: \t{cliente}")
print(f"Total bruto: \t${total_bruto}")
print(f"Total desc: \t${descuento}")
print(f"Iva: \t\t${iva}")
print(f"Total: \t\t${precio_con_descuento + iva}")