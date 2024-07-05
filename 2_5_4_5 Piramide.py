"""
2.5.4 Guía complementaria Ejercicios (Clase 14)
Ejercicio 5
El problema de la pirámide consiste en que, dado una cierta
cantidad de ladrillos, calcular la cantidad de pisos que tendrá la
pirámide.
Una consideración importante es que deben estar todos los
ladrillos necesarios para considerar que hay un nuevo piso. Por
ejemplo, si se tienen 5 ladrillos, todavía se dice que hay dos pisos.
Para evitar confusión es mejor contar los ladrillos disponibles de
abajo hacia arriba.
Indique el algoritmo correcto
"""
#Nota: Este problema lo desarrollé dentro del curso de Python, por eso lo solucioné en ingles
blocks = int(input("Enter the number of blocks: "))
blocks_count = 0
height = 0
while blocks_count<blocks:
    height = height + 1
    blocks_count = blocks_count + height + 1
print("The height of the pyramid:", height)