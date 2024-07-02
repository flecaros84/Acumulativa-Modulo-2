"""
Acomodar el sistema en el siguiente orden, para que permita:
1. Partir con un saldo de 100000 puntos
2. Sistema debe iterar en sentencia While
3. Mostrar un menú de ver mis puntos, gastar mis puntos y
salir
4. Dependiendo de la opción seleccionada, muestre los
puntos disponibles, descuente los puntos dependiendo del
producto seleccionado, y permita salir
5. Cuando se selecciona la opción de gastar mis puntos,
debe mostrar 3 productos
"""
#PuntosAcumulados
sw = 1
puntos = 100000
while sw==1:
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    if op==1:
        print(f"Usted tiene {puntos} puntos")
    elif op==2:
        print("Seleccione el producto a canjear")
        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de: 25.000 puntos")
        print("3.- Disco duro portátil, valor de: 30.000 puntos")
        continu = int(input("Seleccione la opción"))
        if continu==1:
            puntos = puntos-10000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        if continu==2:
            puntos = puntos-25000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
        if continu==3:
            puntos = puntos-30000
            print(f"Canje exitoso, le quedan: ${puntos} puntos")
    elif op==3:
        sw=0