"""
2.3.4.5. De la misma forma del ejercicio anterior, debes crear un formulario con 3
preguntas (4 respuestas por cada pregunta) de un tema a elección, ya sea
películas, series, caricaturas, entre otras.
Asignar puntaje a cada pregunta y dependiendo del puntaje generar una
escala de notas, así cuando los usuarios respondan las 3 preguntas se les
muestra mediante una salida por pantalla su puntaje obtenido y la nota que
equivale.
"""
#Se asigna puntaje de cada pregunta usando diccionarios
alternativa_pregunta1 = {
                        1   : 0,
                        2   : 1,
                        3   : 0,
                        4   : 0
                        }
alternativa_pregunta2 = {
                        1   : 1,
                        2   : 0,
                        3   : 0,
                        4   : 0
                        }
alternativa_pregunta3 = {
                        1   : 0,
                        2   : 0,
                        3   : 1,
                        4   : 0
                        }
print("Test de Python\n______________")
#Para pregunta 1, 2 y 3 se crea un bucle que contiene dentro un if para verificar que se ingrese una alternativa de la lista
#Si se ingresa una de las 4 alternativas, se busca en el diccionario el puntaje asignado a la alternativa y se suma al puntaje total
while True:
    print("Pregunta1: ¿Cuál es la función en Python que se utiliza para imprimir un mensaje en la consola?\n1.display()\n2.print()\n3.show()\n4.println()")
    alternativa_ingresada = int(input("Ingrese N° de alternativa escogida: "))
    if alternativa_ingresada in alternativa_pregunta1:
        break
    print("Error. Valor ingresado no está entre las alternativas")
puntaje_total = alternativa_pregunta1[alternativa_ingresada]
while True:
    print("Pregunta 2: ¿Cuál de las siguientes expresiones en Python devuelve el número entero más grande contenido en una lista?\n1.max(lista)\n2.maximum(lista)\n3.complex\n4.largest(lista)")
    alternativa_ingresada = int(input("Ingrese N° de alternativa escogida: "))
    if alternativa_ingresada in alternativa_pregunta2:
        break
    print("Error. Valor ingresado no está entre las alternativas")
puntaje_total += alternativa_pregunta2[alternativa_ingresada]
while True:
    print("Pregunta 3: ¿Cuál de las siguientes declaraciones sobre las 'expresiones lambda' en Python 3 es verdadera?")
    print("1. Las expresiones lambda pueden contener múltiples líneas de código.")
    print("2. Las expresiones lambda son una forma de definir funciones anónimas en una sola línea de código.")
    print("3. Las expresiones lambda siempre devuelven múltiples valores.")
    print("4. Las expresiones lambda son exclusivas de Python 3.9 y versiones posteriores.")
    alternativa_ingresada = int(input("Ingrese N° de alternativa escogida: "))
    if alternativa_ingresada in alternativa_pregunta3:
        break
    print("Error. Valor ingresado no está entre las alternativas")
puntaje_total += alternativa_pregunta3[alternativa_ingresada]
#Para finalizar se imprime el puntaje total y el cálculo de la equivalencia en nota de 1 a 7
print(f"Usted obtuvo",puntaje_total,"puntos, su nota es un",puntaje_total*2+1)