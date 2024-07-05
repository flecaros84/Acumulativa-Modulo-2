"""
2.5.4 Guía complementaria Ejercicios (Clase 14)
Ejercicio 3
Su antigua profesora de matemáticas del colegio le solicita un
programa de cálculo de áreas y perímetros para poder utilizarlo
con sus alumnos actuales.
Ella desea que las operaciones estén dentro de un menú. En
primer lugar, que los alumnos elijan si quieren calcular el perímetro
o el área. Luego según esa decisión que les permita elegir si
desean esa operación para un círculo, rectángulo o cuadrado.
Finalmente, que pida las medidas según corresponda.
Por otro lado, desea que, si por ejemplo se ingresa al menú de
áreas, el programa se mantenga allí para las siguientes
operaciones a menos que se desee volver al menú principal.
Un ejemplo del menú se presenta en la imagen.
"""
import math
pi = math.pi
print("")
print("Calculadora geométrica")
print("")
while True:
    print("***********Menu************")
    print("1. Calcular Perímetro")
    print("2. Calcular Área")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    print("")
    if opcion == 1:
    #Línea incógnita 1:
        while True:
            print("Calcular Perímetro")
            print("1. Para Círculo")
            print("2. Para Rectángulo")
            print("3. Para Cuadrado")
            print("4. Volver menu principal")
            opcion2 = int(input("Elija una opción: "))
            print("")
            if opcion2 == 1:
                radio = int(input("Ingrese radio del circulo: "))
                #Línea incógnita 2:
                perimetro = 2*pi*radio
                print("Perímetro del Circulo: ", perimetro)
                print("")
            elif opcion2 == 2:
                altura = int(input("Ingrese altura del Rectángulo: "))
                ancho = int(input("Ingrese ancho del Rectángulo: "))
                perimetro = 2 * (altura + ancho)
                print("Perímetro del Rectángulo: ", perimetro)
                print("")
            elif opcion2 == 3:
                lado = int(input("Ingrese lado del Cuadrado: "))
                perimetro = 4 * lado
                print("Perimetro del cuadrado: ", perimetro)
                print("")
            elif opcion2 == 4:
                break
            else:
                print("Elección inválida.")
                print("")
    elif opcion == 2:
        #Línea incógnita 3
        while True:
            print("Calcular Área")
            print("1. Para Círculo")
            print("2. Para Rectángulo")
            print("3. Para Cuadrado")
            print("4. Volver menu principal")
            opcion3 = int(input("Elija una opción: "))
            print("")
            if opcion3 == 1:
                radio = int(input("Ingrese radio del circulo: "))
                area = 3.14 * radio * radio
                print("Área del circulo:", area)
                print("")
            elif opcion3 == 2:
                altura = int(input("Ingrese altura del Rectángulo: "))
                ancho = int(input("Ingrese ancho del Rectángulo: "))
                #Línea incógnita 4
                area = altura * ancho
                print("Área del Rectángulo:", area)
                print("")
            elif opcion3 == 3:
                lado = int(input("Ingrese lado del Cuadrado: "))
                area = lado * lado
                print("Área del Cuadrado:", area)
                print("")
            elif opcion3 == 4:
                break
            else:
                print("Elección inválida.")
                print("")
    elif opcion == 3:
        break
    else:
        print("Elección inválida.")
        print("")