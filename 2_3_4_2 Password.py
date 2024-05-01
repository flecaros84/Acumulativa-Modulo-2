"""
2.3.4.2. Crear un programa de validación de usuario y contraseña (consultar usuario y
contraseña), los únicos dos usuarios conectados son:
User1: pedro Contraseña1: 1234
User2: angel Contraseña2: a4s1
"""
#Diccionario con usuarios y password
usuarios = {
            "pedro"         : "1234",
            "angel"         : "a4s1"
            }
#Loop "Pseudo Do While" para verificar usuario
while True:
    usuario_ingresado = input("Ingrese usuario: ")
    if usuario_ingresado in usuarios:
        break
    print("Usuario incorrecto")
#Loop "Pseudo Do While" para verificar password
while True:
    print("Usuario validado:",usuario_ingresado)
    password_ingresado = input("Ingrese password: ")
    if password_ingresado == usuarios[usuario_ingresado]:
        print("Bienvenido",usuario_ingresado)
        break
    print("Password incorrecto")