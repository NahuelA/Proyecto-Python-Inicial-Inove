#!/usr/bin/env python

"""
Proyecto inicial del curso python brindado por inove ARG

SEGUIMIENTO DE FLOTA
--------------------------

Autor: Nahuel Arrascaeta

Versión: 1.0

Descripción: Programa que permite analizar los movimientos de una flota de vehiculos, el objetivo es analizar la información de los viajes ya realizados.
"""
#importaciones de librerías estandar
import csv
# from os import write
# from typing import Iterable

#creación del archivo sólo con el encabezado
"""
file = open("Proyecto_integrador_python_inicial\seguimiento_flota.csv","w",newline='')

csv_file = csv.DictWriter(file, fieldnames=FIELDNAMES)
csv_file.writeheader()
file.close()
"""

#Variables globales
FIELDNAMES = ["fecha de salida", "patente", "empresa","tiempo recorrido",
              "recaudacion", "fecha de llegada","latitud", "longitud"
             ]
FILE = "seguimiento_flota.csv"

#Función para validar inicio de sesión
def validation(NAME_ADMIN, PASS_ADMIN):
    while True:
        name = str(input("**Ingrese nombre de usuario administrador: "))
        password = str(input("**Ingrese contraseña de administrador: "))
        print("")
                
        if name == NAME_ADMIN and password == PASS_ADMIN:
            print("**Bienvenido {}!!".format(name))
            print("")
            break
        elif name == "exit" or password == "exit":
            exit()
        else:
            print("*Datos de sesión incorrectos, intentelo de nuevo*")
            print("")


#Función para recorrer todo el archivo csv hasta 
#encontrar la fila con la fecha consultada
def get_date(date):
    
    repeat = True
    #Para repetir la función get_date, la variable date_repeat debe ser == a "repeat"
    date_repeat = ""

    while repeat:
        with open(FILE) as file_opn:
            csv_opn = list(csv.DictReader(file_opn))

            #Recorre el archivo csv y verifico si existe la fecha consultada    
            for read_csv_opn in range(len(csv_opn)):
                if csv_opn[read_csv_opn].get("fecha de salida") == date:
                    repeat = False
                    #Retorna el índice del la fila que se modificará
                    return read_csv_opn
                elif date == "exit":
                    exit()
            #Comprobar si la fecha no se encontró
            if csv_opn[read_csv_opn].get("fecha de salida") != date:
                print("*No se ha encontrado ningún registro con esa fecha, vuelve a intentarlo*\n")
                repeat = False
                date_repeat = "repeat"
                return date_repeat


def examp_fieldnames(case):
    #Ejemplos para guiarse a la hora de modificar o crear un registro
    if case == "fecha de salida":
        print("*Ejemplo: DD/MM/YY")
    elif case == "patente":
        print("as203fd")
    elif case == "empresa":
        print("*Correo argentino*")
    elif case == "tiempo recorrido":
        print("*total de horas viajadas*")
    elif case == "recaudacion":
        print("*Total de recaudado por hs*")

#------------------------------------------------------------------------------.
#Herramientas para administradores
#------------------------------------------------------------------------------.
#Modificar un registro
def modify_record():

    repeat = True
    while repeat:

        date = str(input("-Ingrese la fecha del registro que desea modificar: "))
        print("")
        #Recorro el archivo csv y verifico si
        #existe un registro con la fecha indicada
        #Almacenar el valor de retorno en la variable row
        row = get_date(date)
        #Si row es True vuelve a ejecutar el bucle desde el principio
        #Esta condición se cumple si no se encuentra
        #Ninguna fecha de la consultada
        if row == "repeat":
            continue
        #abro el csv y lo almaceno en una matriz
        file_opn = open(FILE)
        csv_opn = list(csv.DictReader(file_opn))

        #Validación de campo existente
        while True:
            record_inp = str(input("-Ingrese el campo que desea modificar: "))
            if FIELDNAMES.count(record_inp) == 1:
                break
            elif record_inp == "exit":
                exit()
            else:
                print("*No existe un campo con ese nombre, intentalo de nuevo*\n")
        while True:
            #Ejemplos para rellenar campos
            examp_fieldnames(record_inp)
            #Ingreso de datos
            data_record = str(input(f"\n-Ingrese los nuevos datos para el campo {record_inp}: "))
            #Modifico los datos del registro elegido
            if data_record == "":
                print("*No se permiten campos vacíos...*")
            elif data_record == "exit":
                exit()
            else:
                break
        #Almaceno datos nuevos
        csv_opn[row][record_inp] = data_record
        file_opn.close

        #Abro el archivo csv para escribir los cambios realizados
        file_opn = open(FILE,"w",newline="")
        
        writer = csv.DictWriter(file_opn, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(csv_opn)
        file_opn.close()

        #Salir de la función o volver a ejecutarla
        while repeat:
            repeat_function = str(input("-Desea modificar otros campos?: ")).capitalize()
            if repeat_function == "Si":
                pass
            elif repeat_function == "No":
                repeat = False
            elif repeat_function == "Exit":
                exit()
            else:
                print("-Ingrese una opción válida...\n")


#crear un registro
def create_record():

    repeat = True
    while repeat:

        print("-Rellene los campos correspondientes para crear un nuevo registro.\n")
        #Recorrer todo el encabezado para rellenar todos los campos
        count_fieldnames = len(FIELDNAMES)
        #Creando lista para los datos del registro
        list_row = []
        
        for field in range(len(FIELDNAMES)):
            #Bucle para evitar campos vacíos
            repeat_field = True
            while repeat_field:
                fields = str(input("-Ingrese los datos del campo *{}*: ".format(FIELDNAMES[field]))).capitalize()
                #Exit para salir
                if fields == "Exit":
                    exit()
                elif fields == "":
                    print("-No se permiten campos vacíos...")
                    continue
                #Almacenamos el nuevo registro en la lista
                data_field = fields
                list_row.append(data_field)
                repeat_field = False
            #Muestra la cantidad de campos restantes para crear un registro
            count_fieldnames -= 1
            print("-Campos restantes: {}\n".format(count_fieldnames))

        #Pasamos los elementos de la variable list_row al diccionario dict_row
        dict_row = dict(zip(FIELDNAMES,list_row))

        #Abrimos el archivo csv para añadir un nuevo registro
        with open(FILE,"a") as csv_open:
                
            writer = csv.DictWriter(csv_open, fieldnames=FIELDNAMES)
            writer.writerow(dict_row)
        #Salir de la función o volver a ejecutarla
        while repeat:
            repeat_create_rcd = str(input("Desea crear otro registro?\n-Si\n-No\n-Exit\n: ")).capitalize()
            if repeat_create_rcd == "Si":
                break
            elif repeat_create_rcd == "No":
                repeat = False
            elif repeat_create_rcd == "Exit":
                exit()
            else:
                print("-Ingrese una opción válida...\n")


#Eliminar un registro
def record_delete():
    repeat = True
    while repeat:
        #Obtiene la fecha de registro y el indice de la fila
        date = str(input("-Ingrese la fecha del registro que desea eliminar: "))
        date_index = get_date(date)
        #Si date_index es True vuelve a ejecutar el bucle desde el principio
        #Esta condición se cumple si no se encuentra
        #Ninguna fecha de la consultada
        if date_index == "repeat":
            continue

        with open(FILE) as file_opn:
            #Abro el csv para eliminar el registro seleccionado
            csv_file = list(csv.DictReader(file_opn))
            csv_file.pop(date_index)
        
        with open(FILE,"w",newline="") as file_opn:
            #Abro el csv para escribir los datos sin el registro eliminado
            writer = csv.DictWriter(file_opn,fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(csv_file)
        
        print("-Eliminación exitosa!")
        #Salir de la función o volver a ejecutarla
        while repeat:
            repeat_delete = str(input("-Desea eliminar más registros?: ")).capitalize()
            if repeat_delete == "Si":
                break
            elif repeat_delete == "No":
                repeat = False
            elif repeat_delete == "Exit":
                exit()
            else:
                print("-Ingrese una opción válida...\n")
                

#Analizar un registro
def analyze_record():

    repeat = True
    while repeat:
        date = str(input(("-Ingrese la fecha del registro que desea Analizar: ")))
        date_index = get_date(date)
        #Si date_index es True vuelve a ejecutar el bucle desde el principio
        #Esta condición se cumple si no se encuentra
        #Ninguna fecha de la consultada
        if date_index == "repeat":
            continue
        #Abrimos el archivo
        with open(FILE) as file_opn:
            csv_file = list(csv.DictReader(file_opn))
            get_record = csv_file[date_index]
            #Analisis del registro:
            #Transformar de hora a minuto:
            time_ = int(csv_file[date_index].get("tiempo recorrido"))
            hs_min = time_*60
            #Total de dinero recaudado:
            cash_ = int(csv_file[date_index].get("recaudacion"))
            cash = cash_*time_
            #Total de viajes realizados
            travels = 0
            #Obtener patente
            patent = csv_file[date_index]["patente"]
            for travel in csv_file:
                if travel.get("patente") == patent:
                    travels += 1

        #Imprimir registro
        print(f"-Registro número {date_index} impreso:")
        print(get_record)
        print(f"-Datos del viaje en la fecha: {date}")
        print(f"Tiempo recorrido en horas: {time_}")
        print(f"-Tiempo recorrido en minutos: {hs_min}")
        print(f"-Dinero recaudado por horas trabajadas: ${cash}")
        print(f"-Viajes realizados del vehículo {patent} : {travels}")
        #Salir de la función o volver a ejecutarla
        while repeat:
            repeat_delete = str(input("-Desea eliminar más registros?: ")).capitalize()
        if repeat_delete == "Si":
            break
        elif repeat_delete == "No":
            repeat = False
        elif repeat_delete == "Exit":
            exit()
        else:
            print("-Ingrese una opción válida...\n")


#------------------------------------------------------------------------------.
#Inicio del programa main
#------------------------------------------------------------------------------.
def main():

    #Pedir al usuario que ingrese como administrador o visitante
    #Variables globales dentro de main
    NAME_ADMIN = "Admin"
    NAME = ""
    PASS_ADMIN = "Contraseña123"
    KEY_1 = False
    KEY_2 = False

    while True:

        print("Ingrese como administrador o como visitante:")
        print("Si es administrador, presione la tecla 'a'")
        print("Si es visitante, presione la tecla 'v'")
        print("Si desea salir, presione la tecla 'x'")

        usuario_input = str(input(": ")).upper()

        if usuario_input == "A":
            #validación módulo
            validation(NAME_ADMIN, PASS_ADMIN)
            KEY_1 = True
            break
        elif usuario_input == "V":
            NAME = str(input("Ingrese su nombre de visitante: "))
            print("")
            KEY_2 = True
            break
        elif usuario_input == "X":
            print("Saliendo del programa...")
            print("")
            exit()
        else:
            print("Ingrese una opción valida...\n")
    
    #bucle para administradores
    while KEY_1:
        print("¿Qué desea realizar? \n-Presione '1' para: Modificar un registro\n-Presione '2' para: Crear un registro \n-Presione '3' para: Eliminar un registro \n-Presione '4' para: Analizar un registro \n-Presione '5' para: Salir \n")

        usuario_input = str(input(": "))
        print("")

        while True:

            if usuario_input == "1":
                #Modificar un registro
                modify_record()
                break
            elif usuario_input == "2":
                #Crear un registro
                create_record()
                break
            elif usuario_input == "3":
                #Eliminar un registro
                record_delete()
                break
            elif usuario_input == "4":
                #analizar registro
                analyze_record()
                pass
            elif usuario_input == "5":
                verify_exit = str(input("Está seguro que desea salir del programa? \n -SI PARA SALIR \n -INGRESE CUALQUIER CARACTER PARA CANCELAR: ")).capitalize()
                if verify_exit == "Si":
                    print(" \n Saliendo del programa...")
                    exit()
                else:
                    print("")
                    break
            else:
                print("Ingresa una opción válida...")

    #bucle para visitantes
    while KEY_2:
        print(f"Bienvenido visitante {NAME}!")
        analyze_record()
        break

if __name__ == "__main__":
    main()