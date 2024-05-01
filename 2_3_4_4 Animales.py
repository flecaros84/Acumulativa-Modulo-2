"""
2.3.4.4. Crear una salida por pantalla con la siguiente información:
¿Cuál de los siguientes animales vive en el agua?
Perro
Cocodrilo
Conejo
Tiburón
Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la
respuesta es Tiburón asignar +1.0 a puntaje, del cualquier
otro caso, no asignar valor, finalmente crear una salida por
pantalla para mostrar el puntaje obtenido.
"""
animales = {
            1   : 0,
            2   : 0.5,
            3   : 0,
            4   : 1.0
            }
while True:
    print("¿Cuál de los siguientes animales vive en el agua?\n1.Perro\n2.Cocodrilo\n3.Conejo\n4.Tiburón")
    animal_ingresado = int(input("Ingrese el N° del animal elegido: "))
    if animal_ingresado in animales:
        break
    print("Error. Valor ingresado no está en lista de animales")
print(f"Usted obtuvo",animales[animal_ingresado],"puntos")