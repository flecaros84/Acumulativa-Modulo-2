#Instrucciones al usuario
print("Cálculadora de Python")
print("---------------------")
print("Operadores Permitidos:")
print("+: Suma")
print("-: Resta")
print("*: Multiplicación")
print("/: División")
print("s: Salir")
#Ingresar primera operación
operacion = str(input("Ingrese su operación: "))
#Definir función calculadora
def calculadora(operacion):
    return float(eval(operacion))
#Ciclo para realizar operaciones
while operacion != "s":
    print("Resultado = " + str(calculadora(operacion)))
    operacion = str(input("Ingrese su operación: "))
input("Presione una tecla para cerrar")