#Se solicita ingresar la temperatura en celsius
celsius = float(input("Ingresa la temperatura en celsius (debe ser mayor al cero absoluto -273.15°C): "))
#Se verifica que la temperatura esté sobre el cero absoluto
while celsius < -273.15:
    print("Error, valor bajo el cero absoluto") 
    celsius = float(input("Ingresa la temperatura en celsius (debe ser mayor al cero absoluto -273.15°C): "))
#Se calcula la temperatura en fahrenheit
fahrenheit = float(celsius*(9/5)+32)
#Se imprime el resultado
print("La temperatura en fahrenheit es: " + str(fahrenheit))
input("Presiona una tecla para finalizar")