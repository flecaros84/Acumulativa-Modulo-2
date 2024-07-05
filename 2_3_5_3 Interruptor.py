"""
Guia 2.3.5. Ejercicio 3
La empresa eléctrica luz de la mañana, desea crear un interruptor de
escalera digital, tal de que sea programable en un circuito diurno.
La idea es que existan 2 interruptores del tipo On - OFF a cada
extremo de una escalera o pasillo permitiendo que se pueda prender o
apagar de cualquiera de los dos extremos.
La lógica involucrada en esto es de un NOT XOR, es decir, la luz se
prenderá sólo si ambos interruptores están en ON, o si ambos
interruptores están en OFF.
"""

#Función que solicita y evalua que valor ingresado no sea erroneo
def circuito(interruptor):
    while True:
        try: 
            reset = interruptor
            interruptor = int(input(f"Ingrese 1 para encender o 0 para apagar (Valor actual {interruptor}): "))
        except ValueError:
            print("Valor debe ser un entero 0 o 1")
            interruptor = reset
        else: 
            if (interruptor != 0 and interruptor != 1) :
                print("Valor debe ser un entero 0 o 1")
                interruptor = reset
            else:
                return interruptor

interruptor1 = 1
interruptor2 = 0
print("Interruptor 1")
interruptor1 = circuito(interruptor1)
print("Interruptor 2")
interruptor2 = circuito(interruptor2)            
if (interruptor1 == interruptor2) :
    print("Prende la luz")
else:
    print("Apaga la luz")