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
from typing import Iterable

#importaciones de librerías propias
#import Modulos.Modulos

#creación del archivo sólo con el encabezado
"""
file = open("Proyecto_integrador_python_inicial\seguimiento_flota.csv","w",newline='')

csv_file = csv.DictWriter(file, fieldnames=FIELDNAMES)
csv_file.writeheader()
file.close()
"""

#Variables globales
FIELDNAMES = ["fecha de salida", "patente", "empresa","tiempo recorrido", "recaudacion", "fecha de llegada","latitud", "longitud"]
FILE = "seguimiento_flota.csv"

#Función para validar inicio de sesión
def validation(NAME_ADMIN, PASS_ADMIN):
    while True:
        name = str(input("Ingrese nombre de usuario administrador: "))
        password = str(input("Ingrese contraseña de administrador: "))
        print("")
                
        if name == NAME_ADMIN and password == PASS_ADMIN:
            print("Bienvenido {}!!".format(name))
            print("")
            break
        elif name == "exit" or password == "exit":
            exit()
        else:
            print("Datos de sesión incorrectos, intentelo de nuevo")
            print("")
#Función para recorrer todo el archivo csv hasta 
# encontrarla fila con la fecha consultada
def iteracion_get_date(date): # NOTE: --> Acá mandale get_date nomas ;D
    # NOTE: Excelente la función.
    repeat = 1
    with open(FILE) as file_opn:
        csv_opn = list(csv.DictReader(file_opn))
        
        #Recorre el archivo csv y verifico si existe la fecha consultada
        for read_csv_opn in range(len(csv_opn)):
            if csv_opn[read_csv_opn].get("fecha de salida") == date:
                break
            else:
                print("No se ha encontrado ningún registro con esa fecha, vuelve a intentarlo\n")
                repeat = 0
        #Retorna el índice de la fila en la que se encuentra
        #el valor que deseamos modificar
        return read_csv_opn, repeat

#------------------------------------------------------------------------------.
#Herramientas para administradores
#------------------------------------------------------------------------------.

#Modificar un registro
def modify_record():

    date = str(input("Ingrese la fecha del registro que desea modificar: "))
    print("")
    #Recorro el archivo csv y verifico si 
    #existe un registro con la fecha indicada
    iteracion_get_date(date)
    
    #Obtengo el return[1] de la funcíon iteración_get_date
    repeat = iteracion_get_date(date)[1]
    #si dicha función me retorna 1 entonces no repito la función modify_record()
    #En cambio si la función retorna 0 utilizo la recursividad y vuelvo
    #a llamar a la función modify_record()
    if repeat == 0:
        modify_record()
    #abro el csv y lo almaceno en una matriz
    file_opn = open(FILE)
    csv_opn = list(csv.DictReader(file_opn))

    #Validación de campo existente
    while True:
        record_inp = str(input("Ingrese el campo que desea modificar: "))
        if FIELDNAMES.count(record_inp) == 1:
            break
        else:
            print("No existe un campo con ese nombre, intentalo de nuevo\n")
        
    data_record = str(input("\nIngrese los nuevos datos para el campo {}: ".format(record_inp))).capitalize()3

    row = iteracion_get_date(date)[0]
    #Modifico los datos del registro elegido
    if data_record == "":
        csv_opn[row][record_inp] = ""
    else:
        csv_opn[row][record_inp] = data_record
    file_opn.close

    #Abro el archivo csv para escribir los cambios realizados
    file_opn = open(FILE,"w",newline="")
    
    writer = csv.DictWriter(file_opn, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(csv_opn)
    
    file_opn.close()

    #Para repetir la función
    repeat_function = str(input("Desea modificar otros campos?: ")).capitalize()
    if repeat_function == "Si":
        modify_record()
    elif repeat_function == "Exit" or repeat_function == "No" or date == "exit" or data_record == "Exit" or record_inp == "exit":
        exit()


#crar un registro
def create_record():

    print("Rellene los campos correspondientes para crear un nuevo registro.\n'SI ALGÚN CAMPO QUEDA VACÍO SE LO TOMARÁ COMO NONE'\n")

    #recorrer todo el encabezado para rellenar todos los campos
    count_fieldnames = len(FIELDNAMES)
    #Creando lista para los datos del registro
    list_row = []
    
    for field in range(len(FIELDNAMES)):
        
        fields = str(input("Ingrese los datos del campo *{}*: ".format(FIELDNAMES[field]))).capitalize()
        if fields == "Exit":
            exit()
        #Almacenamos el nuevo registro en la lista
        data_field = fields
        list_row.append(data_field)
        
        #Muestra la cantidad de campos restantes para crear un registro
        count_fieldnames = count_fieldnames - 1
        print("Campos restantes: {}\n".format(count_fieldnames))

    #Pasamos los elementos de la variable list_row al diccionario dict_row
    # NOTE: Acá podes crear el diccionario a partir de las dos listas con ZIP:
    # dict_row = dict(zip(FIELDNAMES, list_row))
    # Pero solo si FIELDNAMES y list_row tienen la misma cantidad de elementos, sino tenes que limitarlo vos con el slicing:
    # dict_row = dict(zip(FIELDNAMES[0:7], list_row[0:7]))
    # Probalo :D    
    dict_row = {FIELDNAMES[0]:list_row[0],FIELDNAMES[1]:list_row[1],FIELDNAMES[2]:list_row[2],FIELDNAMES[3]:list_row[3],FIELDNAMES[4]:list_row[4],FIELDNAMES[5]:list_row[5],FIELDNAMES[6]:list_row[6],FIELDNAMES[7]:list_row[7]}

    #Abrimos el archivo csv para añadir un nuevo registro
    with open(FILE,"a") as csv_open:
            
        writer = csv.DictWriter(csv_open, fieldnames=FIELDNAMES)
        writer.writerow(dict_row)
    
    while True:
        repeat_function = str(input("Desea crear otro registro?\n-Si\n-No\n-Exit\n: ")).capitalize()
        
        if repeat_function == "Si":
            create_record()
        elif repeat_function == "No":
            break
        else:
            print("Ingresa una opción válida...\n")


#Eliminar un registro
def record_delete():
    inp_delete = str(input("Ingrese la fecha del registro que desea eliminar: ")).upper()

    if inp_delete == "":
        print("Ingrese una fecha válida...")
        record_delete()
    elif inp_delete == "EXIT":
        exit()
    
    file_open = open(FILE, "a", newline="")
    csv_file = list(csv.DictWriter(file_open, fieldnames=FIELDNAMES))

    for record in range(len(csv_file)):
        pass
#------------------------------------------------------------------------------.
#Inicio del programa main
#------------------------------------------------------------------------------.
def main():

    #Pedir al usuario que ingrese como administrador o visitante

    #Variables globales dentro de main
    NAME_ADMIN = "Admin"
    PASS_ADMIN = "Contraseña123"
    KEY_1 = False
    KEY_2 = False

    print("Ingrese como administrador o como visitante:")
    print("Si es administrador, presione la tecla 'a'")
    print("Si es visitante, presione la tecla 'v'")
    print("Si desea salir, presione la tecla 'x'")

    usuario_input = str(input(": ")).upper()

    while True:

        if usuario_input == "A":
            #validación módulo
            validation(NAME_ADMIN, PASS_ADMIN)
            KEY_1 = True
            break
        elif usuario_input == "V":
            name = str(input("Ingrese su nombre de visitante: "))
            print("")
            KEY_2 = True
            break
        elif usuario_input == "X":
            print("Saliendo del programa...")
            print("")
            exit()
        else:
            print("Ingrese una opción valida...")
            print("")
    
    #bucle para administradores
    while KEY_1:
        # NOTE: Meté el mensaje en un string largo con triple comillas ''' hola bla bla bla '''
        # Así podes hacer saltos de línea tranquilo sin estar fuera del PEP8
        print("¿Qué desea realizar? \n-Presione '1' para: Modificar un registro\n-Presione '2' para: Crear un registro \n-Presione '3' para: Eliminar un registro \n-Presione '4' para: Analizar un registro \n-Presione '5' para: Salir \n")

        usuario_input = str(input(": ")) # NOTE: Todo en ingles o todo en castellano XD
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
                #analyze_record()
                pass
            elif usuario_input == "5":
                # NOTE: Meté el mensaje en un string largo con triple comillas ''' hola bla bla bla '''
                # Así podes hacer saltos de línea tranquilo sin estar fuera del PEP8
                verify_exit = str(input("Está seguro que desea salir del programa? \n -SI PARA SALIR \n -INGRESE CUALQUIER CARACTER PARA CANCELAR: ")).capitalize()

                if verify_exit == "Si":
                    print(" \n Saliendo del programa...")
                    exit()
                else:
                    print("")
                    break
        continue

    #bucle para visitantes
    while KEY_2:
        pass

if __name__ == "__main__":
    main()
