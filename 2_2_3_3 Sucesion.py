"""
Una sucesión numérica es un conjunto ordenado de elementos que pueden ser números, letras o figuras o una combinación de las anteriores. 
Estos elementos se caracterizan por seguir una regla deformación. Determine la secuencia que genera el siguiente programa
"""
numero = 0
print(numero)
siguiente = 1
print(siguiente)
"""
1//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
2//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
3//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
4//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
5//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
6//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)
7//
numero = numero + siguiente
print(numero)
siguiente = numero + siguiente
print(siguiente)

#El ciclo anterior puede sintetizarse en un código más simple
"""
for contador in range(7):
    numero = numero + siguiente
    print(numero)
    siguiente = numero + siguiente
    print(siguiente)