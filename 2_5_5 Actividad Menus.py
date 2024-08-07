"""
2.5.5 Actividad menús registro de usuarios
Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
1) iniciar sesión
2) registrar usuario
3) salir
Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
ambas con valor inicial vacío, ejemplo:
 usuario1= None
 usuario2=None
 usuario3=None
 contrasena1= None
 contrasena2=None
 contrasena3= None
Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar
que es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
menú:
1) Realizar llamada
2) Enviar correo electrónico
3) Cerrar sesión
Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
tamaño es de 9 dígitos (ejemplo: 985447561).
La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
“@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
Finalmente cerrar sesión, volverá al menú principal.
El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si
ocurre esto, entonces el sistema emite un error y vuelve a solicitar la opción.
Recuerde utilizar try Exception en caso de ser necesario.
"""

def login():
    global usuario1
    global usuario2
    global usuario3
    global contrasena1
    global contrasena2
    global contrasena3
    usuario = input("Ingrese su número de usuario: ")
    password = input("Ingrese su contraseña: ")
    if(usuario == usuario1):
        if(password == contrasena1):
            return usuario1
        else:
            print("Contraseña invalida")
    elif(usuario == usuario2):
        if(password == contrasena2):
                return usuario2
        else:
            print("Contraseña invalida")
    elif(usuario == usuario3):
        if(password == contrasena3):
                return usuario3
        else:
            print("Contraseña invalida")                   

def registar_usuario():
    global usuario1
    global usuario2
    global usuario3
    global contrasena1
    global contrasena2
    global contrasena3
    if (usuario1==None):
        usuario1 = input("Ingrese nombre de usuario a registrar:")
        contrasena1 = input(f"Ingrese contraseña para {usuario1}: ")
        return
    elif(usuario2==None):    
        usuario2 = input("Ingrese nombre de usuario a registrar:")
        contrasena2 = input(f"Ingrese contraseña para {usuario2}: ")
        return
    elif(usuario3==None):    
        usuario3 = input("Ingrese nombre de usuario a registrar:")
        contrasena3 = input(f"Ingrese contraseña de {usuario3}")
        return
    else:
        print("No es posible registrar más usuarios")
        return

global usuario1
global usuario2
global usuario3
global contrasena1
global contrasena2
global contrasena3
usuario1=None
usuario2=None
usuario3=None
contrasena1=None
contrasena2=None
contrasena3=None
while True:
    print("Menu de Inicio")
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")
    try: 
        opcion = int(input("Ingrese su opción:"))
    except ValueError:
        print("Opción incorrecta")
    else:
        if opcion ==1:
            if usuario1==None and usuario2==None and usuario3==None:
                print("No existen usuarios registrados")
            else:
                usuario = login()
                if usuario != None:
                    while True:
                        print("Menu de Usuario")
                        print("1) Realizar llamada")
                        print("2) Enviar correo electrónico")
                        print("3) Cerrar sesión")
                        try:
                            opcion2 = int(input("Ingrese su opción:"))
                        except ValueError:
                            print("Opción incorrecta")
                        else:
                            if opcion2 == 1:
                                celular = input("Ingrese el número de celular: ")
                                if celular.startswith("9") and len(celular)==9:
                                    print("Llamada realizada")
                                else:
                                    print("Número de celular incorrecto")
                            elif opcion2 == 2:
                                correo = input("Ingrese su correo electrónico: ")
                                while True:
                                    if "@" in correo:
                                        break
                                    else:
                                        print("Correo incorrecto")
                                        correo = input("Ingrese su correo electrónico: ")
                                mensaje = input("Ingrese el mensaje a enviar: ")
                                print("Correo enviado")
                            elif opcion2 == 3:
                                break
                            else:
                                print("Opción incorrecta")
        elif opcion == 2:
            registar_usuario()
        elif opcion ==3:
            break
        else:
            print("Opción Incorrecta")

            




