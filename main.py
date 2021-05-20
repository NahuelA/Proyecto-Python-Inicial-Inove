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

#funciones 

def validation(NAME_ADMIN, PASS_ADMIN,KEY):
    while True:
        name = str(input("Ingrese nombre de usuario administrador: "))
        password = str(input("Ingrese contraseña de administrador: "))
        print("")
                
        if name == NAME_ADMIN and password == PASS_ADMIN:
            print("Bienvenido {}".format(name))
            print("")
            KEY = True
            break
        elif name == "exit" or password == "exit":
            exit()
        else:
            print("Datos de sesión incorrectos, intentelo de nuevo")
            print("")


#Herramientas para administradores

#Modificar un registro
def modify_record():

    date = str(input("Ingrese la fecha del registro que desea modificar: "))
    print("")

    file = open(FILE,"a")
    csv_file = list(csv.DictWriter((file), fieldnames=FIELDNAMES))

    for i in csv_file:
        #validación si existe un registro con esa fecha
        if date == i.get("fecha de salida"):

            record = str(input("Ingrese el campo que desea modificar: "))
            for i in FIELDNAMES:
                #validación si en el encabezado existe un campo con dicho nombre
                if i == record:
                    data = str(input("Ingrese los nuevos datos para el campo {} : ".format(i)))
                    
                    get_record = csv_file.get(record)
                    if data == "":
                        get_record = ""
                    else:
                        get_record = data
                    break
            break
    file.close()
    
    #Para repetir la función
    repeat_function = str(input("Desea modificar otros campos?: ")).upper()
    if repeat_function == "SI":
        modify_record()
    elif repeat_function == "EXIT":
        exit()


#crar un registro
def create_record():

    print("Rellene los campos correspondientes para crear un nuevo registro.\n 'SI ALGÚN CAMPO QUEDA VACÍO SE LO TOMARÁ COMO NONE'")

    #recorrer todo el encabezado para rellenar todos los campos
    count_fieldnames = len(FIELDNAMES)
    for i in range(len(FIELDNAMES)):
        
        fields = str(input("Ingrese los datos del campo {}: ").format(FIELDNAMES[i]))

        #Creando fila para el nuevo registro
        row = {FIELDNAMES[i]:fields}
        #LLamando la función para escribir la fila dentro del csv

        with open(FILE,"a", newline="") as csv_open:
            
            writer = csv.DictWriter(csv_open, fieldnames=FIELDNAMES)
            writer.writerow(row)
        
        repeat_function = str(input("Desea crear otro registro?: ")).upper()
        if repeat_function == "SI":
            create_record()
        elif repeat_function == "EXIT":
            exit()

        #Muestra la cantidad de campos restantes para crear un registro
        count_fieldnames = count_fieldnames - 1
        print("Campos restantes: {}".format(count_fieldnames))


#Inicio del programa



def main():

    #Pedir al usuario que ingrese como administrador o visitante

    # variables globales
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
            validation(NAME_ADMIN, PASS_ADMIN, KEY_1)
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
        print("¿Qué desea realizar?")
        print("Presione '1' para: Modificar un registro")
        print("Presione '2' para: Crear un registro")
        print("Presione '3' para: Eliminar un registro")
        print("Presione '4' para: Analizar un registro")
        print("Presione '5' para: Salir")

        usuario_input = str(input(": ")).upper()

        while True:

            if usuario_input == "1":
                #modificar un registro
                pass

    
    #bucle para visitantes
    while KEY_2:
        pass

if __name__ == "__main__":
    main()

modify_record()