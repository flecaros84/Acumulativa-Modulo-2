#1.Ingreso de datos del trabajador:
#   El usuario ingresa el nombre del trabajador, su sueldo base y el número de horas extras trabajadas en el mes.
#   Validar que el nombre del trabajador no esté vacío y que tenga una longitud máxima de 30 caracteres.

def Ingreso_Trabajador():
    while True:
        nombre_trabajador = input("Ingrese nombre del trabajador: ")
        if nombre_trabajador == "":
            print("ERROR. El nombre de trabajador no debe estar vacio")
        elif len(nombre_trabajador) > 30:
            print("ERROR. El largo del nombre debe ser menor o igual a 30 caracteres")
        else:
            return nombre_trabajador

#   Validar que el sueldo base y las horas extras sean valores numéricos positivos.        
def Ingreso_Sueldo_Base():
    while True:
        try:
            sueldo_base = int(input("Ingrese el sueldo base: "))
        except ValueError:
            print("ERROR. Debe ingresar un entero positivo")
        else:
            if sueldo_base <= 0:
                print("ERROR. Debe ingresar un entero positivo")
            else:
                return sueldo_base
            
def Ingreso_Horas_Extras():
    while True:
        try:
            horas_extras = int(input("Ingrese horas extras: "))
        except ValueError:
            print("ERROR. Debe ingresar un real positivo")
        else:
            if horas_extras < 0:
                print("ERROR. Debe ingresar un número mayor o igual a 0")
            else:
                return horas_extras
            
#2. Cálculo de la liquidación:

def Calculo_Liquidacion(nombre_trabajador,sueldo_base,horas_extras):
#   Calcular el pago por horas extras, considerando que cada hora extra se paga un 50% más que una hora normal.
    pagoxhoras_extras = round((sueldo_base)/180 * horas_extras * 1.5)
#   Calcular el total de ingresos, sumando el sueldo base y el pago por horas extras.
    total_ingresos = sueldo_base + pagoxhoras_extras
#   Calcular el descuento por fonasa, que corresponde al 7% del total de ingresos.
    descuentoxfonasa = round(total_ingresos*0.07)
#   Calcular el descuento por AFP, que corresponde al 10% del total de ingresos.
    descuentoxafp = round(total_ingresos*0.1)
    # Calcular el sueldo neto a pagar, restando el descuento por seguridad social al total de ingresos.
    sueldo_neto = total_ingresos - descuentoxfonasa - descuentoxafp
    #Aplico separador de miles a las cifras en CLP para facilitar su lectura
    sueldo_base = '{:,.0f}'.format(sueldo_base)
    pagoxhoras_extras = '{:,.0f}'.format(pagoxhoras_extras)
    total_ingresos = '{:,.0f}'.format(total_ingresos)
    descuentoxfonasa = '{:,.0f}'.format(descuentoxfonasa)
    descuentoxafp = '{:,.0f}'.format(descuentoxafp)
    sueldo_neto = '{:,.0f}'.format(sueldo_neto)
#Mostrar la liquidación:
#   Mostrar un desglose de la liquidación, incluyendo el nombre del trabajador, su sueldo base, el pago por horas extras, el total de
#   ingresos, el descuento por seguridad social y el sueldo neto a pagar, todo ordenado y bien presentado.
    print("LIQUIDACIÓN DE SUELDO")
    print(f"Nombre trabajador       :",nombre_trabajador,sep ='\t')
    print(f"Horas Extras            :",horas_extras,sep ='\t')
    print(f"(+) Sueldo Base         :",sueldo_base,sep ='\t')
    print(f"(+) Pago x Horas Extras :",pagoxhoras_extras,sep ='\t')
    print(f"(=) Total Ingresos      :",total_ingresos,sep ='\t')
    print(f"(-) Descuento x Fonasa  :",descuentoxfonasa,sep ='\t')
    print(f"(-) Descuento x AFP     :",descuentoxafp,sep ='\t')
    print(f"(=) Sueldo Neto         :",sueldo_neto,sep ='\t')
#Generar archivo de liquidación:
#- Crear un archivo de texto (.txt) o un documento de Word (.docx) con los datos de la liquidación del trabajador.
#- El archivo generado debe incluir el nombre del trabajador, su sueldo base, el pago por horas extras, el total de ingresos, los descuentos por
#FONASA y AFP, y el sueldo neto a pagar, todo de forma ordenada y bien presentada.
#- El nombre del archivo generado debe seguir el formato "liquidacion_[nombre_trabajador].txt"    
    while True:
        try:
            archivo = open(f"liquidacion_{nombre_trabajador}.txt","r")
            archivo = open(f"liquidacion_{nombre_trabajador}.txt","w")
            archivo.write("LIQUIDACION DE SUELDOS\n")
            archivo.write(f"Nombre trabajador       :\t{nombre_trabajador}\n")
            archivo.write(f"Horas Extras            :\t{horas_extras}\n")
            archivo.write(f"(+) Sueldo Base         :\t{sueldo_base}\n")
            archivo.write(f"(+) Pago x Horas Extras :\t{pagoxhoras_extras}\n")
            archivo.write(f"(=) Total Ingresos      :\t{total_ingresos}\n")
            archivo.write(f"(-) Descuento x Fonasa  :\t{descuentoxfonasa}\n")
            archivo.write(f"(-) Descuento x AFP     :\t{descuentoxafp}\n")
            archivo.write(f"(=) Sueldo Neto         :\t{sueldo_neto}\n")
            print(f"Se ha escrito el archivo liquidación_{nombre_trabajador}.txt")
            return
        except FileNotFoundError:
            print(f"El archivo no existe. Creando liquidacion_{nombre_trabajador}.txt")
            archivo = open(f"liquidacion_{nombre_trabajador}.txt", "x")

#Utilizar estructuras de repetición para permitir el cálculo de múltiples liquidaciones.
while True:
    nombre_trabajador = Ingreso_Trabajador()
    sueldo_base = Ingreso_Sueldo_Base()
    horas_extras = Ingreso_Horas_Extras()
    Calculo_Liquidacion(nombre_trabajador,sueldo_base,horas_extras)
    print("¿Desea generar otra liquidación?")
    continuar = input("Ingrese S para continuar o cualquier otro valor para salir: ")
    if continuar.lower() != "s":
        break
     
            



