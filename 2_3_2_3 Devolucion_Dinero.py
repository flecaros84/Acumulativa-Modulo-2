"""
¿Qué mensaje nos imprimirá el sistema, si nos devuelve una devolución
de dinero de $120.000, e ingresamos el user “duoc123”, y el pass
“123duoc”?.

"""
#Devolución Dinero
user = input("Ingrese el usuario: ")
pwd = input("Ingrese su password: ")
if user == "duoc" and pwd == "123duoc":
    valorDev = int(input("Bienvenido, Ingrese el valor a devolver: "))
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolución de dinero")
    else:
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print ("Error en contraseña")
"""
Respuesta: Se obtiene el mensaje "Se dará la máxima urgencia a su devolución de dinero". 
Parece haber un error en la guia resulta en AVA, pues ahi se dice que el output es:
"El caso ha quedado registrado, le informaremos lo antes posible"
"""