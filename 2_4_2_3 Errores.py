"""
2.4.2 Guía Ejercicios Ciclos o bucles
EJERCICIO 3
Construye un programa que tenga como objetivo el solo ser referente para la utili-
zación de captura de errores por medio excepciones, el programa debe capturar
error de valores, y división por cero.
"""

def evaluar_dividendo():
    while True:
        try:
            numero = float(input("Ingrese el dividendo: "))
        except ValueError:
            print("Los argumentos deben ser números reales")
        else: 
            return numero

def evaluar_divisor():
    while True:
        try:
            numero = float(input("Ingrese el divisor: "))
        except ValueError:
            print("Los argumentos deben ser números reales")
        else:
            return numero

print("Programa de división")
dividendo = evaluar_dividendo()
divisor = evaluar_divisor()
try:
    resultado = dividendo/divisor
except ZeroDivisionError:
    print("El divisor no puede ser cero")
except ValueError:
    print("Los argumentos deben ser números reales")
else:
    print(f"El resultado es = {resultado}")
    