#ValorNetoDeUnProducto
producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: "))
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")
#¿Por qué se debe ocupar tipo de dato Float para calcular el IVA?
#Porque el IVA es un número real o float 19% o 0.19