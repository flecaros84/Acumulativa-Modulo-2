"""
2.3.4.1. Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es
mayor de edad o no.
"""
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted tiene",edad,"años, por tanto es mayor de edad" )
else:
    print("Usted tiene",edad,"años, por tanto es menor de edad")