# 4)Contador de vocales: Crea un programa que solicite al usuario una cadena de texto y
#cuente la cantidad de vocales presentes en la cadena. Imprime el resultado.
cadena = input("Ingrese una cadena de texto: ").upper()
contador = 0
for letra in cadena:
    # Chequear si la letra es una vocal
    if letra in ['A', 'E', 'I', 'O', 'U']:
        contador+=1
print(contador)