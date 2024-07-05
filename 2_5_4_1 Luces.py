"""
2.5.4 Guía complementaria Ejercicios (Clase 14)
Ejercicio 1.

Una empresa de IoT está desarrollando un sistema de control a
través de internet de las luces de las viviendas. De esta forma las
personas podrán controlar sus luces desde cualquier lugar.
Para el desarrollo de este objetivo, usted es contratado tal de que
programe una aplicación con dicha funcionalidad.
Usted programa un menú con las distintas opciones que se
aprecian en la imagen.
La particularidad de este sistema es que con la misma opción se
puede encender o apagar la luz, si se trata de una luz en
particular, puesto que así lo solicitó la empresa.
"""
def encender_apagar(sitio):
    if sitio == 0:
        sitio = 1
        return sitio
    elif sitio == 1:
        sitio = 0
        return sitio

def estado(sitio):
    if sitio == 0:
        return "apagado"
    elif sitio == 1:
        return "encendido"
        
patio   = 0
sala    = 0
pasillo = 0
jardin  = 0

while True:
    try:
        print(f"1. Encender/Apagar luces Patio   ({estado(patio)})")
        print(f"2. Encender/Apagar luces Sala    ({estado(sala)})")
        print(f"3. Encender/Apagar luces Pasillo ({estado(pasillo)})")
        print(f"4. Encender/Apagar luces Jardín  ({estado(jardin)})")
        print("5. Encender todo")
        print("6. Apagar todo")
        print("7. Salir del Sistema")
        opcion = int(input("Ingrese su opción: "))
    except ValueError:
        print("Opción debe ser un entero entre 1 y 7")
    else:
        if opcion ==0 or opcion >7:
            print("Opción debe ser un entero entre 1 y 7")
        else: 
            match opcion:
                case 1:
                    patio=encender_apagar(patio)
                    print(f"El patio esta {estado(patio)}")
                case 2:
                    sala=encender_apagar(sala)
                    print(f"El sala esta {estado(sala)}")
                case 3:
                    pasillo=encender_apagar(pasillo)
                    print(f"El sala esta {estado(pasillo)}")
                case 4:
                    jardin=encender_apagar(jardin)
                    print(f"El sala esta {estado(jardin)}")
                case 5:
                    patio = sala = pasillo = jardin = 1
                    print("Todas las luces estan encendidas")
                case 6:
                    patio = sala = pasillo = jardin = 0
                    print("Todas las luces estan apagadas")
                case 7:
                    break

                



