"""
5)Validador de contraseña: Escribe un programa que pida al usuario una contraseña. La
contraseña debe tener al menos 8 caracteres, al menos una letra mayúscula, al menos una
letra minúscula y al menos un número. Imprime un mensaje indicando si la contraseña
cumple con estos requisitos.
"""
#Input de contraseña
contraseña = input("Ingresa contraseña: ")
#Inicio de variables booleanas de chequeo
check_mayuscula = False
check_minuscula = False
check_largo = False
check_numero = False
#Chequeo largo de contraseña
if len(contraseña)>=8:
        check_largo = True
#Chequeo de mayusculas, minusculas y digitos
for caracter in contraseña:
    if caracter.isupper() == True:
        check_mayuscula = True
    if caracter.islower() == True:
        check_minuscula = True
    if caracter.isdigit() == True:
        check_numero = True
#Validación de contraseña
if check_largo==True and check_mayuscula==True and check_minuscula==True and check_numero==True:
    print("Contraseña cumple los requisitos")
else: 
    print("Contraseña no cumple los requisitos")