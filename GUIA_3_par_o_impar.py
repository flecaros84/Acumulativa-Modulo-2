import math
numero = float(input("Ingresa un número: "))
residuo = math.remainder(numero,2)
if residuo == 0:
    print("El número es par")
else:
    print("El número es impar")
input("Presiona una tecla para finalizar")