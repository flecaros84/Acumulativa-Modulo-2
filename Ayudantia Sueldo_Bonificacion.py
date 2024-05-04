"""
Especificaciones:
● El programa debe solicitar al usuario ingresar el nombre del empleado, su antigüedad en años
y su evaluación de desempeño (que puede ser 'A', 'B' o 'C').
● Las bonificaciones se calcularán según los siguientes criterios:
○ Si la antigüedad es menor a 2 años:
■ Evaluación 'A': bonificación del 5% del sueldo base.
■ Evaluación 'B': bonificación del 3% del sueldo base.
■ Evaluación 'C': no hay bonificación.
○ Si la antigüedad está entre 2 y 5 años (inclusive):
■ Evaluación 'A': bonificación del 8% del sueldo base.
■ Evaluación 'B': bonificación del 5% del sueldo base.
■ Evaluación 'C': bonificación del 2% del sueldo base.
○ Si la antigüedad es mayor a 5 años:
■ Evaluación 'A': bonificación del 12% del sueldo base.
■ Evaluación 'B': bonificación del 8% del sueldo base.
■ Evaluación 'C': bonificación del 5% del sueldo base.
● El sueldo base para todos los empleados es de $1,000,000.
● El programa debe calcular el monto de la bonificación y el sueldo total del empleado (sueldo
base + bonificación).
● Los resultados deben mostrarse al usuario de manera clara y legible, con el monto de la
bonificación y el sueldo total formateados en pesos chilenos.
Requerimientos adicionales:
● El programa debe utilizar estructuras de control de flujo como if, elif y else para determinar la
bonificación correspondiente según la antigüedad y la evaluación de desempeño.
● Se deben utilizar funciones para modularizar el código y hacerlo más legible.
● El programa debe manejar adecuadamente los tipos de datos y realizar las conversiones
necesarias.
● Se deben agregar comentarios en el código para explicar su funcionamiento.
"""
def calcular_sueldo(nombre,antiguedad,evaluacion):
    if antiguedad < 2:
        match evaluacion:
            case "A":
                factor_bono = 0.05
            case "B":
                factor_bono = 0.03
            case "C":
                factor_bono = 0
    elif antiguedad>=2 and antiguedad<=5:
        match evaluacion:
            case "A":
                factor_bono = 0.08
            case "B":
                factor_bono = 0.05
            case "C":
                factor_bono = 0.02
    elif antiguedad>5:
        match evaluacion:
            case "A":
                factor_bono = 0.12
            case "B":
                factor_bono = 0.08
            case "C":
                factor_bono = 0.05
    bonificacion = int(sueldo*factor_bono)
    print(f"Bonificación para el empleado {nombre}")
    print("Sueldo Base:",f"{sueldo:,}")
    print(f"Bonificación ({factor_bono*100}%):",f"{bonificacion:,}")
    print("Sueldo Total:", f"{sueldo+bonificacion:,}")

sueldo = 1000000
nombre_empleado = input("Ingrese el nombre del empleado: ")
antiguedad_empleado = int(input("Ingrese la antiguedad del empleado en años: "))
while True:
    evaluacion_empleado = input("Ingrese la evaluación del empleado:").upper()
    if evaluacion_empleado == "A" or evaluacion_empleado =="B" or evaluacion_empleado =="C":
        break
    print("Valor ingresado incorrecto. Debe ser A, B o C")
calcular_sueldo(nombre_empleado,antiguedad_empleado,evaluacion_empleado)