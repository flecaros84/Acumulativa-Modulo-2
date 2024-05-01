"""
2.3.4.3. Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3
notas (cada nota tiene la misma ponderación), finalmente indicar con una
salida de pantalla “Aprobado” en el caso de que el promedio sea igual o
mayor a 4.0.
"""
#Importamos la libreria estadistica que permite promediar datos de listas
import statistics
#Construí este algoritmo para que pueda promediar cualquier número de notas
n_notas = int(input("Ingresa el n° de notas a promediar:"))
lista_notas = []
#En este loop se van acumulando notas en la lista_notas, admitiendo solo valores entre 1 y 7.
for contador in range(n_notas):
    while True:
        nota_ingresada = float(input((f"Ingresa la nota {contador+1}:")))
        if nota_ingresada >=1 and nota_ingresada <=7:
            lista_notas.append(nota_ingresada)
            break
        else: 
            print("Nota ingresada debe estar en el rango [1,7]")
#Promediamos y definimos si el alumno aprueba o no.
promedio = statistics.mean(lista_notas)  
print("El promedio es:",promedio)
if promedio >= 4:
    print("APROBADO")
else:
    print("REPROBADO")