"""
Guia 2.3.5. Ejercicio 4 
La empresa desarrolladora de juegos “El banquete”, te ha solicitado un
prototipo de juego de aventuras.
Tu muy emocionado comienzas a programar, puesto que tienes una
gran idea que te ha seguido durante años.
Dentro del juego puedes moverte a la derecha si presionas ‘d’, a la
izquierda si presionas ‘a’ o hacia adelante si presionas ‘w’
Una preview del juego se aprecia en la imagen:
Debes revisar si el algoritmo es correcto con respecto a las
indicaciones del mismo juego.
"""
print("Juego: La gran aventura")
print("Puedes moverte a la derecha 'd', a la izquierda 'a' o hacia adelante 'w'")
print("Inicia la aventura")
opcion = input("Corres hacia la montaña nevada. Un ruido te detiene (muevete hacia un lado):")
if opcion == "a":
    print("Ves un gran oso que comienza a avanzar a ti")
    opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado. ")
    if opcion == "w":
        print("Te mueves un poco hacia adelante y el oso te mata")
    elif opcion == "a":
        print("Te mueves hacia la izquierda y una planta carnívora de come.")
    else:
        print("Te mueves un poco hacia la derecha y ves un túnel que te lleva al siguiente nivel.")
elif opcion == "d":
    print("Ves una serpiente que está a 30 centímetros de tu pie.")
    opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado: ")
    if opcion == "w":
        print("Te mueves un poco hacia adelante y la serpiente te muerde y mueres con dolor.")
    elif opcion == "a":
        print("Te mueves hacia la izquierda y una planta carnívora de come.")
    else:
        print("Te mueves un poco hacia la derecha y ves un túnel que te lleva al siguiente nivel.")
else :
    print("Ves una luz que se acerca a ti")
    opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado: ")
    if opcion == "w":
        print("Te mueves un poco hacia adelante y el túnel te lleva al siguiente nivel")
    elif opcion == "a":
        print("Te mueves hacia la izquierda y una planta carnívora de come.")
    else:
        print("Te mueves un poco hacia la derecha y un león se abalanza contra ti y te come el cuello.")
print("Fin de la partida, gracias por jugar.")