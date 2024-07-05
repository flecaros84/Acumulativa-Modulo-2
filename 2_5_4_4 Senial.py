"""
2.5.4 Guía complementaria Ejercicios (Clase 14)
Ejercicio 4
El procesamiento de señales digitales o DSP (sigla en inglés de
digital signal processing) es la manipulación matemática de una
señal de información para modificarla o mejorarla en algún
sentido. Este está caracterizado por la representación en el
dominio del tiempo discreto, en el dominio frecuencia discreta, u
otro dominio discreto de señales por medio de una secuencia de
números o símbolos y el procesado de esas señales. (wiki pedia)
La empresa DSP Research, le pide simular en ython la señal
digital compuesta que se presenta en la image.
Esta señal periódica se puede dividir en 4 partes: exponencial,
senoidal, escalón, y continua. Es importante que la secuencia de
los algortimos sea la correcta para generar la señal solicitada.
(Determine el orden correcto del algoritmo para generarla.)
"""
import time
while True:
    espacios = ""
    linea = "*"
    for i in range(11):
        print(linea)
        espacios += " "
        linea = espacios + linea
        time.sleep(0.05)
    for i in range(14):
        print(linea)
        espacios = " "
        linea = linea[i:]
        time.sleep(0.05)
        linea = "*"
        espacio = " "
    for i in range(22):
        linea +=" *"
        espacio +=" "
        print(linea)
        espacio +="*"
    for i in range(14):
        print(espacio)
        time.sleep(0.05)
        print(linea)