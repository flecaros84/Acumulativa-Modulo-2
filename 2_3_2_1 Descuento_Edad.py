"""
Reordenar los códigos con el fin que el sistema valide:
Rango de edad entre 0 y menor que 18 años. Descuento de
50%
Rango de edad entre 18 y menor que 30 años. Descuento de
20%
Mayor o igual a 60 años. Descuento de 90%
"""
#Descuento por edad
edad = int(input ("Ingrese su edad"))
if edad > 0 and edad > 18:
    print (f"Edad: {edad} ,tiene descuento de un 50% ")
elif edad >= 18 and edad < 30:
    print (f"Edad: {edad} ,tiene descuento de un 20%")
elif edad >= 60:
    print (f"Edad: {edad} ,tiene descuento de un 90%")
else:
    print (f"Edad: {edad} ,no aplica descuento")