def Ingreso_Trabajador():
    while True:
        nombre_trabajador = input("Ingrese nombre del trabajador: ")
        if nombre_trabajador == "":
            print("ERROR. El nombre de trabajador no debe estar vacio")
        elif len(nombre_trabajador) > 30:
            print("ERROR. El largo del nombre debe ser menor o igual a 30 caracteres")
        else:
            return nombre_trabajador
        
ingreso_trabajador = Ingreso_Trabajador()